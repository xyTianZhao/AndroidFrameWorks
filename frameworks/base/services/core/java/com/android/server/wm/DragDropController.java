/*
 * Copyright (C) 2017 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.android.server.wm;

import static com.android.server.wm.WindowManagerDebugConfig.DEBUG_DRAG;
import static com.android.server.wm.WindowManagerDebugConfig.SHOW_LIGHT_TRANSACTIONS;
import static com.android.server.wm.WindowManagerDebugConfig.TAG_WM;

import android.annotation.NonNull;
import android.content.ClipData;
import android.os.Binder;
import android.os.Handler;
import android.os.IBinder;
import android.os.Looper;
import android.os.Message;
import android.util.Slog;
import android.view.Display;
import android.view.IWindow;
import android.view.SurfaceControl;
import android.view.SurfaceSession;
import android.view.View;

import com.android.internal.util.Preconditions;
import com.android.server.wm.WindowManagerInternal.IDragDropCallback;

import java.util.concurrent.atomic.AtomicReference;

/**
 * Managing drag and drop operations initiated by View#startDragAndDrop.
 * 管理由 ViewstartDragAndDrop 启动的拖放操作
 */
class DragDropController {
    private static final float DRAG_SHADOW_ALPHA_TRANSPARENT = .7071f;
    private static final long DRAG_TIMEOUT_MS = 5000;

    // Messages for Handler.
    static final int MSG_DRAG_END_TIMEOUT = 0;
    static final int MSG_TEAR_DOWN_DRAG_AND_DROP_INPUT = 1;
    static final int MSG_ANIMATION_END = 2;

    /**
     * Drag state per operation.
     * Needs a lock of {@code WindowManagerService#mWindowMap} to read this. Needs both locks of
     * {@code mWriteLock} and {@code WindowManagerService#mWindowMap} to update this.
     * The variable is cleared by {@code #onDragStateClosedLocked} which is invoked by DragState
     * itself, thus the variable can be null after calling DragState's methods.
     */
    private DragState mDragState;

    private WindowManagerService mService;
    private final Handler mHandler;

    /**
     * Callback which is used to sync drag state with the vendor-specific code.
     */
    @NonNull private AtomicReference<IDragDropCallback> mCallback = new AtomicReference<>(
            new IDragDropCallback() {});

    boolean dragDropActiveLocked() {
        return mDragState != null && !mDragState.isClosing();
    }

    void registerCallback(IDragDropCallback callback) {
        Preconditions.checkNotNull(callback);
        mCallback.set(callback);
    }

    DragDropController(WindowManagerService service, Looper looper) {
        mService = service;
        mHandler = new DragHandler(service, looper);
    }

    void sendDragStartedIfNeededLocked(WindowState window) {
        mDragState.sendDragStartedIfNeededLocked(window);
    }

    IBinder performDrag(SurfaceSession session, int callerPid, int callerUid, IWindow window,
            int flags, SurfaceControl surface, int touchSource, float touchX, float touchY,
            float thumbCenterX, float thumbCenterY, ClipData data) {
        if (DEBUG_DRAG) {
            Slog.d(TAG_WM, "perform drag: win=" + window + " surface=" + surface + " flags=" +
                            Integer.toHexString(flags) + " data=" + data);
        }

        /*** 空实现，默认返回 true */
        final IBinder dragToken = new Binder();
        final boolean callbackResult = mCallback.get().prePerformDrag(window, dragToken,
                touchSource, touchX, touchY, thumbCenterX, thumbCenterY, data);
        try {
            synchronized (mService.mGlobalLock) {
                try {
                    if (!callbackResult) {
                        Slog.w(TAG_WM, "IDragDropCallback rejects the performDrag request");
                        return null;
                    }

                    /*** 正在拖拽，屏蔽其他起始拖拽 */
                    if (dragDropActiveLocked()) {
                        Slog.w(TAG_WM, "Drag already in progress");
                        return null;
                    }

                    // 当前 window 合法，并且可以接收 touch 事件
                    final WindowState callingWin = mService.windowForClientLocked(
                            null, window, false);
                    if (callingWin == null || callingWin.cantReceiveTouchInput()) {
                        Slog.w(TAG_WM, "Bad requesting window " + window);
                        return null;  // !!! TODO: throw here?
                    }

                    // !!! TODO: if input is not still focused on the initiating window, fail
                    // the drag initiation (e.g. an alarm window popped up just as the application
                    // called performDrag()

                    // !!! TODO: extract the current touch (x, y) in screen coordinates.  That
                    // will let us eliminate the (touchX,touchY) parameters from the API.

                    // !!! FIXME: put all this heavy stuff onto the mHandler looper, as well as
                    // the actual drag event dispatch stuff in the dragstate

                    // !!! TODO(multi-display): support other displays

                    final DisplayContent displayContent = callingWin.getDisplayContent();
                    if (displayContent == null) {
                        Slog.w(TAG_WM, "display content is null");
                        return null;
                    }

                    /*** 拖拽背景是否透明 */
                    final float alpha = (flags & View.DRAG_FLAG_OPAQUE) == 0 ?
                            DRAG_SHADOW_ALPHA_TRANSPARENT : 1;
                    final IBinder winBinder = window.asBinder();
                    IBinder token = new Binder();
                    /*** 创建本次拖拽的状态机 */
                    mDragState = new DragState(mService, this, token, surface, flags, winBinder);
                    surface = null;
                    mDragState.mPid = callerPid;
                    mDragState.mUid = callerUid;
                    mDragState.mOriginalAlpha = alpha;
                    mDragState.mToken = dragToken;
                    mDragState.mDisplayContent = displayContent;

                    final Display display = displayContent.getDisplay();
                    /*** 注册输入拦截，切换窗口焦点 */
                    if (!mCallback.get().registerInputChannel(
                            mDragState, display, mService.mInputManager,
                            callingWin.mInputChannel)) {
                        Slog.e(TAG_WM, "Unable to transfer touch focus");
                        return null;
                    }

                    mDragState.mData = data;
                    /**
                     * 调用每个可见的窗口会话，通知其有关拖动的信息
                     * notify {@link android.view.DragEvent#ACTION_DRAG_STARTED}
                     */
                    mDragState.broadcastDragStartedLocked(touchX, touchY);
                    mDragState.overridePointerIconLocked(touchSource);
                    // remember the thumb offsets for later
                    mDragState.mThumbOffsetX = thumbCenterX;
                    mDragState.mThumbOffsetY = thumbCenterY;

                    // Make the surface visible at the proper location
                    final SurfaceControl surfaceControl = mDragState.mSurfaceControl;
                    if (SHOW_LIGHT_TRANSACTIONS) Slog.i(TAG_WM, ">>> OPEN TRANSACTION performDrag");

                    /*** 显示 drag 窗口 */
                    final SurfaceControl.Transaction transaction = mDragState.mTransaction;
                    transaction.setAlpha(surfaceControl, mDragState.mOriginalAlpha);
                    transaction.setPosition(
                            surfaceControl, touchX - thumbCenterX, touchY - thumbCenterY);
                    transaction.show(surfaceControl);
                    displayContent.reparentToOverlay(transaction, surfaceControl);
                    callingWin.scheduleAnimation();

                    if (SHOW_LIGHT_TRANSACTIONS) {
                        Slog.i(TAG_WM, "<<< CLOSE TRANSACTION performDrag");
                    }

                    /**
                     * 这里会先发送 {@link android.view.DragEvent#ACTION_DRAG_ENTERED}
                     * 在发送 {@link android.view.DragEvent#ACTION_DRAG_LOCATION}
                     */
                    mDragState.notifyLocationLocked(touchX, touchY);
                } finally {
                    if (surface != null) {
                        surface.release();
                    }
                    if (mDragState != null && !mDragState.isInProgress()) {
                        mDragState.closeLocked();
                    }
                }
            }
            return dragToken;    // success!
        } finally {
            mCallback.get().postPerformDrag();
        }
    }

    void reportDropResult(IWindow window, boolean consumed) {
        IBinder token = window.asBinder();
        if (DEBUG_DRAG) {
            Slog.d(TAG_WM, "Drop result=" + consumed + " reported by " + token);
        }

        mCallback.get().preReportDropResult(window, consumed);
        try {
            synchronized (mService.mGlobalLock) {
                if (mDragState == null) {
                    // Most likely the drop recipient ANRed and we ended the drag
                    // out from under it.  Log the issue and move on.
                    Slog.w(TAG_WM, "Drop result given but no drag in progress");
                    return;
                }

                if (mDragState.mToken != token) {
                    // We're in a drag, but the wrong window has responded.
                    Slog.w(TAG_WM, "Invalid drop-result claim by " + window);
                    throw new IllegalStateException("reportDropResult() by non-recipient");
                }

                // The right window has responded, even if it's no longer around,
                // so be sure to halt the timeout even if the later WindowState
                // lookup fails.
                mHandler.removeMessages(MSG_DRAG_END_TIMEOUT, window.asBinder());
                WindowState callingWin = mService.windowForClientLocked(null, window, false);
                if (callingWin == null) {
                    Slog.w(TAG_WM, "Bad result-reporting window " + window);
                    return;  // !!! TODO: throw here?
                }

                mDragState.mDragResult = consumed;
                mDragState.endDragLocked();
            }
        } finally {
            mCallback.get().postReportDropResult();
        }
    }

    void cancelDragAndDrop(IBinder dragToken, boolean skipAnimation) {
        if (DEBUG_DRAG) {
            Slog.d(TAG_WM, "cancelDragAndDrop");
        }

        mCallback.get().preCancelDragAndDrop(dragToken);
        try {
            synchronized (mService.mGlobalLock) {
                if (mDragState == null) {
                    Slog.w(TAG_WM, "cancelDragAndDrop() without prepareDrag()");
                    throw new IllegalStateException("cancelDragAndDrop() without prepareDrag()");
                }

                if (mDragState.mToken != dragToken) {
                    Slog.w(TAG_WM,
                            "cancelDragAndDrop() does not match prepareDrag()");
                    throw new IllegalStateException(
                            "cancelDragAndDrop() does not match prepareDrag()");
                }

                mDragState.mDragResult = false;
                mDragState.cancelDragLocked(skipAnimation);
            }
        } finally {
            mCallback.get().postCancelDragAndDrop();
        }
    }

    /**
     * Handles motion events.
     * @param keepHandling Whether if the drag operation is continuing or this is the last motion
     *          event.
     * @param newX X coordinate value in dp in the screen coordinate
     * @param newY Y coordinate value in dp in the screen coordinate
     */
    void handleMotionEvent(boolean keepHandling, float newX, float newY) {
        synchronized (mService.mGlobalLock) {
            if (!dragDropActiveLocked()) {
                // The drag has ended but the clean-up message has not been processed by
                // window manager. Drop events that occur after this until window manager
                // has a chance to clean-up the input handle.
                return;
            }

            if (keepHandling) {
                mDragState.notifyMoveLocked(newX, newY);
            } else {
                mDragState.notifyDropLocked(newX, newY);
            }
        }
    }

    void dragRecipientEntered(IWindow window) {
        if (DEBUG_DRAG) {
            Slog.d(TAG_WM, "Drag into new candidate view @ " + window.asBinder());
        }
    }

    void dragRecipientExited(IWindow window) {
        if (DEBUG_DRAG) {
            Slog.d(TAG_WM, "Drag from old candidate view @ " + window.asBinder());
        }
    }

    /**
     * Sends a message to the Handler managed by DragDropController.
     */
    void sendHandlerMessage(int what, Object arg) {
        mHandler.obtainMessage(what, arg).sendToTarget();
    }

    /**
     * Sends a timeout message to the Handler managed by DragDropController.
     */
    void sendTimeoutMessage(int what, Object arg) {
        mHandler.removeMessages(what, arg);
        final Message msg = mHandler.obtainMessage(what, arg);
        mHandler.sendMessageDelayed(msg, DRAG_TIMEOUT_MS);
    }

    /**
     * Notifies the current drag state is closed.
     */
    void onDragStateClosedLocked(DragState dragState) {
        if (mDragState != dragState) {
            Slog.wtf(TAG_WM, "Unknown drag state is closed");
            return;
        }
        mDragState = null;
    }

    private class DragHandler extends Handler {
        /**
         * Lock for window manager.
         */
        private final WindowManagerService mService;

        DragHandler(WindowManagerService service, Looper looper) {
            super(looper);
            mService = service;
        }

        @Override
        public void handleMessage(Message msg) {
            switch (msg.what) {
                case MSG_DRAG_END_TIMEOUT: {
                    final IBinder win = (IBinder) msg.obj;
                    if (DEBUG_DRAG) {
                        Slog.w(TAG_WM, "Timeout ending drag to win " + win);
                    }

                    synchronized (mService.mGlobalLock) {
                        // !!! TODO: ANR the drag-receiving app
                        if (mDragState != null) {
                            mDragState.mDragResult = false;
                            mDragState.endDragLocked();
                        }
                    }
                    break;
                }

                case MSG_TEAR_DOWN_DRAG_AND_DROP_INPUT: {
                    if (DEBUG_DRAG)
                        Slog.d(TAG_WM, "Drag ending; tearing down input channel");
                    final DragState.InputInterceptor interceptor =
                            (DragState.InputInterceptor) msg.obj;
                    if (interceptor == null) return;
                    synchronized (mService.mGlobalLock) {
                        interceptor.tearDown();
                    }
                    break;
                }

                case MSG_ANIMATION_END: {
                    synchronized (mService.mGlobalLock) {
                        if (mDragState == null) {
                            Slog.wtf(TAG_WM, "mDragState unexpectedly became null while " +
                                    "plyaing animation");
                            return;
                        }
                        mDragState.closeLocked();
                    }
                    break;
                }
            }
        }
    }
}

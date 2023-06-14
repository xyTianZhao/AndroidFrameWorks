/*___Generated_by_IDEA___*/

/*
 * This file is auto-generated.  DO NOT MODIFY.
 */
package android.net.ipmemorystore;
/** {@hide} */
public interface IOnStatusListener extends android.os.IInterface
{
  /** Default implementation for IOnStatusListener. */
  public static class Default implements android.net.ipmemorystore.IOnStatusListener
  {
    /**
         * The operation has completed with the specified status.
         */
    @Override public void onComplete(android.net.ipmemorystore.StatusParcelable status) throws android.os.RemoteException
    {
    }
    @Override
    public android.os.IBinder asBinder() {
      return null;
    }
  }
  /** Local-side IPC implementation stub class. */
  public static abstract class Stub extends android.os.Binder implements android.net.ipmemorystore.IOnStatusListener
  {
    private static final java.lang.String DESCRIPTOR = "android.net.ipmemorystore.IOnStatusListener";
    /** Construct the stub at attach it to the interface. */
    public Stub()
    {
      this.attachInterface(this, DESCRIPTOR);
    }
    /**
     * Cast an IBinder object into an android.net.ipmemorystore.IOnStatusListener interface,
     * generating a proxy if needed.
     */
    public static android.net.ipmemorystore.IOnStatusListener asInterface(android.os.IBinder obj)
    {
      if ((obj==null)) {
        return null;
      }
      android.os.IInterface iin = obj.queryLocalInterface(DESCRIPTOR);
      if (((iin!=null)&&(iin instanceof android.net.ipmemorystore.IOnStatusListener))) {
        return ((android.net.ipmemorystore.IOnStatusListener)iin);
      }
      return new android.net.ipmemorystore.IOnStatusListener.Stub.Proxy(obj);
    }
    @Override public android.os.IBinder asBinder()
    {
      return this;
    }
    @Override public boolean onTransact(int code, android.os.Parcel data, android.os.Parcel reply, int flags) throws android.os.RemoteException
    {
      java.lang.String descriptor = DESCRIPTOR;
      switch (code)
      {
        case INTERFACE_TRANSACTION:
        {
          reply.writeString(descriptor);
          return true;
        }
        case TRANSACTION_onComplete:
        {
          data.enforceInterface(descriptor);
          android.net.ipmemorystore.StatusParcelable _arg0;
          if ((0!=data.readInt())) {
            _arg0 = android.net.ipmemorystore.StatusParcelable.CREATOR.createFromParcel(data);
          }
          else {
            _arg0 = null;
          }
          this.onComplete(_arg0);
          return true;
        }
        default:
        {
          return super.onTransact(code, data, reply, flags);
        }
      }
    }
    private static class Proxy implements android.net.ipmemorystore.IOnStatusListener
    {
      private android.os.IBinder mRemote;
      Proxy(android.os.IBinder remote)
      {
        mRemote = remote;
      }
      @Override public android.os.IBinder asBinder()
      {
        return mRemote;
      }
      public java.lang.String getInterfaceDescriptor()
      {
        return DESCRIPTOR;
      }
      /**
           * The operation has completed with the specified status.
           */
      @Override public void onComplete(android.net.ipmemorystore.StatusParcelable status) throws android.os.RemoteException
      {
        android.os.Parcel _data = android.os.Parcel.obtain();
        try {
          _data.writeInterfaceToken(DESCRIPTOR);
          if ((status!=null)) {
            _data.writeInt(1);
            status.writeToParcel(_data, 0);
          }
          else {
            _data.writeInt(0);
          }
          boolean _status = mRemote.transact(Stub.TRANSACTION_onComplete, _data, null, android.os.IBinder.FLAG_ONEWAY);
          if (!_status && getDefaultImpl() != null) {
            getDefaultImpl().onComplete(status);
            return;
          }
        }
        finally {
          _data.recycle();
        }
      }
      public static android.net.ipmemorystore.IOnStatusListener sDefaultImpl;
    }
    static final int TRANSACTION_onComplete = (android.os.IBinder.FIRST_CALL_TRANSACTION + 0);
    public static boolean setDefaultImpl(android.net.ipmemorystore.IOnStatusListener impl) {
      // Only one user of this interface can use this function
      // at a time. This is a heuristic to detect if two different
      // users in the same process use this function.
      if (Stub.Proxy.sDefaultImpl != null) {
        throw new IllegalStateException("setDefaultImpl() called twice");
      }
      if (impl != null) {
        Stub.Proxy.sDefaultImpl = impl;
        return true;
      }
      return false;
    }
    public static android.net.ipmemorystore.IOnStatusListener getDefaultImpl() {
      return Stub.Proxy.sDefaultImpl;
    }
  }
  /**
       * The operation has completed with the specified status.
       */
  public void onComplete(android.net.ipmemorystore.StatusParcelable status) throws android.os.RemoteException;
}

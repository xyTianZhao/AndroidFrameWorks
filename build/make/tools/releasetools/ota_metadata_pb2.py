# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ota_metadata.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ota_metadata.proto',
  package='build.tools.releasetools',
  syntax='proto3',
  serialized_options=_b('H\003'),
  serialized_pb=_b('\n\x12ota_metadata.proto\x12\x18\x62uild.tools.releasetools\"X\n\x0ePartitionState\x12\x16\n\x0epartition_name\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65vice\x18\x02 \x03(\t\x12\r\n\x05\x62uild\x18\x03 \x03(\t\x12\x0f\n\x07version\x18\x04 \x01(\t\"\xce\x01\n\x0b\x44\x65viceState\x12\x0e\n\x06\x64\x65vice\x18\x01 \x03(\t\x12\r\n\x05\x62uild\x18\x02 \x03(\t\x12\x19\n\x11\x62uild_incremental\x18\x03 \x01(\t\x12\x11\n\ttimestamp\x18\x04 \x01(\x03\x12\x11\n\tsdk_level\x18\x05 \x01(\t\x12\x1c\n\x14security_patch_level\x18\x06 \x01(\t\x12\x41\n\x0fpartition_state\x18\x07 \x03(\x0b\x32(.build.tools.releasetools.PartitionState\"c\n\x08\x41pexInfo\x12\x14\n\x0cpackage_name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x03\x12\x15\n\ris_compressed\x18\x03 \x01(\x08\x12\x19\n\x11\x64\x65\x63ompressed_size\x18\x04 \x01(\x03\"E\n\x0c\x41pexMetadata\x12\x35\n\tapex_info\x18\x01 \x03(\x0b\x32\".build.tools.releasetools.ApexInfo\"\xf8\x03\n\x0bOtaMetadata\x12;\n\x04type\x18\x01 \x01(\x0e\x32-.build.tools.releasetools.OtaMetadata.OtaType\x12\x0c\n\x04wipe\x18\x02 \x01(\x08\x12\x11\n\tdowngrade\x18\x03 \x01(\x08\x12P\n\x0eproperty_files\x18\x04 \x03(\x0b\x32\x38.build.tools.releasetools.OtaMetadata.PropertyFilesEntry\x12;\n\x0cprecondition\x18\x05 \x01(\x0b\x32%.build.tools.releasetools.DeviceState\x12<\n\rpostcondition\x18\x06 \x01(\x0b\x32%.build.tools.releasetools.DeviceState\x12#\n\x1bretrofit_dynamic_partitions\x18\x07 \x01(\x08\x12\x16\n\x0erequired_cache\x18\x08 \x01(\x03\x12\x15\n\rspl_downgrade\x18\t \x01(\x08\x1a\x34\n\x12PropertyFilesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"4\n\x07OtaType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x06\n\x02\x41\x42\x10\x01\x12\t\n\x05\x42LOCK\x10\x02\x12\t\n\x05\x42RICK\x10\x03\x42\x02H\x03\x62\x06proto3')
)



_OTAMETADATA_OTATYPE = _descriptor.EnumDescriptor(
  name='OtaType',
  full_name='build.tools.releasetools.OtaMetadata.OtaType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AB', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLOCK', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BRICK', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=972,
  serialized_end=1024,
)
_sym_db.RegisterEnumDescriptor(_OTAMETADATA_OTATYPE)


_PARTITIONSTATE = _descriptor.Descriptor(
  name='PartitionState',
  full_name='build.tools.releasetools.PartitionState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='partition_name', full_name='build.tools.releasetools.PartitionState.partition_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device', full_name='build.tools.releasetools.PartitionState.device', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='build', full_name='build.tools.releasetools.PartitionState.build', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='build.tools.releasetools.PartitionState.version', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=136,
)


_DEVICESTATE = _descriptor.Descriptor(
  name='DeviceState',
  full_name='build.tools.releasetools.DeviceState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device', full_name='build.tools.releasetools.DeviceState.device', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='build', full_name='build.tools.releasetools.DeviceState.build', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='build_incremental', full_name='build.tools.releasetools.DeviceState.build_incremental', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='build.tools.releasetools.DeviceState.timestamp', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sdk_level', full_name='build.tools.releasetools.DeviceState.sdk_level', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='security_patch_level', full_name='build.tools.releasetools.DeviceState.security_patch_level', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partition_state', full_name='build.tools.releasetools.DeviceState.partition_state', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=139,
  serialized_end=345,
)


_APEXINFO = _descriptor.Descriptor(
  name='ApexInfo',
  full_name='build.tools.releasetools.ApexInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='package_name', full_name='build.tools.releasetools.ApexInfo.package_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='build.tools.releasetools.ApexInfo.version', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_compressed', full_name='build.tools.releasetools.ApexInfo.is_compressed', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='decompressed_size', full_name='build.tools.releasetools.ApexInfo.decompressed_size', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=347,
  serialized_end=446,
)


_APEXMETADATA = _descriptor.Descriptor(
  name='ApexMetadata',
  full_name='build.tools.releasetools.ApexMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='apex_info', full_name='build.tools.releasetools.ApexMetadata.apex_info', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=448,
  serialized_end=517,
)


_OTAMETADATA_PROPERTYFILESENTRY = _descriptor.Descriptor(
  name='PropertyFilesEntry',
  full_name='build.tools.releasetools.OtaMetadata.PropertyFilesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='build.tools.releasetools.OtaMetadata.PropertyFilesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='build.tools.releasetools.OtaMetadata.PropertyFilesEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=918,
  serialized_end=970,
)

_OTAMETADATA = _descriptor.Descriptor(
  name='OtaMetadata',
  full_name='build.tools.releasetools.OtaMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='build.tools.releasetools.OtaMetadata.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wipe', full_name='build.tools.releasetools.OtaMetadata.wipe', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='downgrade', full_name='build.tools.releasetools.OtaMetadata.downgrade', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='property_files', full_name='build.tools.releasetools.OtaMetadata.property_files', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='precondition', full_name='build.tools.releasetools.OtaMetadata.precondition', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='postcondition', full_name='build.tools.releasetools.OtaMetadata.postcondition', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='retrofit_dynamic_partitions', full_name='build.tools.releasetools.OtaMetadata.retrofit_dynamic_partitions', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='required_cache', full_name='build.tools.releasetools.OtaMetadata.required_cache', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spl_downgrade', full_name='build.tools.releasetools.OtaMetadata.spl_downgrade', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_OTAMETADATA_PROPERTYFILESENTRY, ],
  enum_types=[
    _OTAMETADATA_OTATYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=520,
  serialized_end=1024,
)

_DEVICESTATE.fields_by_name['partition_state'].message_type = _PARTITIONSTATE
_APEXMETADATA.fields_by_name['apex_info'].message_type = _APEXINFO
_OTAMETADATA_PROPERTYFILESENTRY.containing_type = _OTAMETADATA
_OTAMETADATA.fields_by_name['type'].enum_type = _OTAMETADATA_OTATYPE
_OTAMETADATA.fields_by_name['property_files'].message_type = _OTAMETADATA_PROPERTYFILESENTRY
_OTAMETADATA.fields_by_name['precondition'].message_type = _DEVICESTATE
_OTAMETADATA.fields_by_name['postcondition'].message_type = _DEVICESTATE
_OTAMETADATA_OTATYPE.containing_type = _OTAMETADATA
DESCRIPTOR.message_types_by_name['PartitionState'] = _PARTITIONSTATE
DESCRIPTOR.message_types_by_name['DeviceState'] = _DEVICESTATE
DESCRIPTOR.message_types_by_name['ApexInfo'] = _APEXINFO
DESCRIPTOR.message_types_by_name['ApexMetadata'] = _APEXMETADATA
DESCRIPTOR.message_types_by_name['OtaMetadata'] = _OTAMETADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PartitionState = _reflection.GeneratedProtocolMessageType('PartitionState', (_message.Message,), {
  'DESCRIPTOR' : _PARTITIONSTATE,
  '__module__' : 'ota_metadata_pb2'
  # @@protoc_insertion_point(class_scope:build.tools.releasetools.PartitionState)
  })
_sym_db.RegisterMessage(PartitionState)

DeviceState = _reflection.GeneratedProtocolMessageType('DeviceState', (_message.Message,), {
  'DESCRIPTOR' : _DEVICESTATE,
  '__module__' : 'ota_metadata_pb2'
  # @@protoc_insertion_point(class_scope:build.tools.releasetools.DeviceState)
  })
_sym_db.RegisterMessage(DeviceState)

ApexInfo = _reflection.GeneratedProtocolMessageType('ApexInfo', (_message.Message,), {
  'DESCRIPTOR' : _APEXINFO,
  '__module__' : 'ota_metadata_pb2'
  # @@protoc_insertion_point(class_scope:build.tools.releasetools.ApexInfo)
  })
_sym_db.RegisterMessage(ApexInfo)

ApexMetadata = _reflection.GeneratedProtocolMessageType('ApexMetadata', (_message.Message,), {
  'DESCRIPTOR' : _APEXMETADATA,
  '__module__' : 'ota_metadata_pb2'
  # @@protoc_insertion_point(class_scope:build.tools.releasetools.ApexMetadata)
  })
_sym_db.RegisterMessage(ApexMetadata)

OtaMetadata = _reflection.GeneratedProtocolMessageType('OtaMetadata', (_message.Message,), {

  'PropertyFilesEntry' : _reflection.GeneratedProtocolMessageType('PropertyFilesEntry', (_message.Message,), {
    'DESCRIPTOR' : _OTAMETADATA_PROPERTYFILESENTRY,
    '__module__' : 'ota_metadata_pb2'
    # @@protoc_insertion_point(class_scope:build.tools.releasetools.OtaMetadata.PropertyFilesEntry)
    })
  ,
  'DESCRIPTOR' : _OTAMETADATA,
  '__module__' : 'ota_metadata_pb2'
  # @@protoc_insertion_point(class_scope:build.tools.releasetools.OtaMetadata)
  })
_sym_db.RegisterMessage(OtaMetadata)
_sym_db.RegisterMessage(OtaMetadata.PropertyFilesEntry)


DESCRIPTOR._options = None
_OTAMETADATA_PROPERTYFILESENTRY._options = None
# @@protoc_insertion_point(module_scope)

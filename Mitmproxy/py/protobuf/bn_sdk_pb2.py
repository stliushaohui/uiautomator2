# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bn_sdk.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='bn_sdk.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('\312\002\034modules\\collect\\parse_app\\pb\342\002!modules\\collect\\parse_app\\pb_meta'),
  serialized_pb=_b('\n\x0c\x62n_sdk.proto\"\xb5\x01\n\x15SDK3PushLogDeviceInfo\x12\x0c\n\x04\x61\x64Id\x18\x01 \x01(\t\x12\r\n\x05\x61ndId\x18\x02 \x01(\t\x12\n\n\x02\x63h\x18\x03 \x01(\t\x12\n\n\x02\x64n\x18\x04 \x01(\t\x12\x0b\n\x03\x64id\x18\x05 \x01(\t\x12\x0c\n\x04imei\x18\x06 \x01(\t\x12\x0b\n\x03net\x18\x07 \x01(\t\x12\x0b\n\x03osv\x18\x08 \x01(\t\x12\n\n\x02ss\x18\t \x01(\t\x12\x0c\n\x04sdkv\x18\n \x01(\t\x12\n\n\x02gv\x18\x0b \x01(\t\x12\x0c\n\x04oaid\x18\x0c \x01(\t\"W\n\x13SDK3PushLogUserInfo\x12\r\n\x05level\x18\x01 \x01(\x05\x12\x0b\n\x03rid\x18\x02 \x01(\t\x12\n\n\x02rn\x18\x03 \x01(\t\x12\x0b\n\x03sid\x18\x04 \x01(\t\x12\x0b\n\x03uid\x18\x05 \x01(\t\"\xca\x01\n\x10SDK3PushLogStart\x12\"\n\x02\x64i\x18\x01 \x01(\x0b\x32\x16.SDK3PushLogDeviceInfo\x12\r\n\x05\x61ppid\x18\x02 \x01(\t\x12\n\n\x02os\x18\x03 \x01(\t\x12\n\n\x02pn\x18\x04 \x01(\t\x12\x10\n\x08packdate\x18\x05 \x01(\t\x12+\n\x05\x61info\x18\x06 \x03(\x0b\x32\x1c.SDK3PushLogStart.AinfoEntry\x1a,\n\nAinfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"r\n\x0fSDK3PushLogGame\x12\"\n\x02\x64i\x18\x01 \x01(\x0b\x32\x16.SDK3PushLogDeviceInfo\x12 \n\x02ui\x18\x02 \x01(\x0b\x32\x14.SDK3PushLogUserInfo\x12\r\n\x05\x61ppid\x18\x03 \x01(\t\x12\n\n\x02os\x18\x04 \x01(\t\"x\n\x15SDK3PushLogRoleUpdate\x12\"\n\x02\x64i\x18\x01 \x01(\x0b\x32\x16.SDK3PushLogDeviceInfo\x12 \n\x02ui\x18\x02 \x01(\x0b\x32\x14.SDK3PushLogUserInfo\x12\r\n\x05\x61ppid\x18\x03 \x01(\t\x12\n\n\x02os\x18\x04 \x01(\t\"\x9f\x01\n\x0eSDK3PushLogDur\x12\"\n\x02\x64i\x18\x01 \x01(\x0b\x32\x16.SDK3PushLogDeviceInfo\x12\r\n\x05\x61ppid\x18\x02 \x01(\t\x12\n\n\x02os\x18\x03 \x01(\t\x12\x0b\n\x03uid\x18\x04 \x01(\t\x12\x0b\n\x03rid\x18\x05 \x01(\t\x12\x0b\n\x03sid\x18\x06 \x01(\t\x12\x0e\n\x06lifeid\x18\x07 \x01(\t\x12\x0b\n\x03\x64ur\x18\x08 \x01(\x05\x12\n\n\x02st\x18\t \x01(\x05\"\xa4\x01\n\x11SDK3PushLogPeriod\x12\"\n\x02\x64i\x18\x01 \x01(\x0b\x32\x16.SDK3PushLogDeviceInfo\x12\r\n\x05\x61ppid\x18\x02 \x01(\t\x12\n\n\x02os\x18\x03 \x01(\t\x12\x0b\n\x03uid\x18\x04 \x01(\t\x12\x0b\n\x03rid\x18\x05 \x01(\t\x12\x0b\n\x03sid\x18\x06 \x01(\t\x12\x0e\n\x06lifeid\x18\x07 \x01(\t\x12\x0e\n\x06period\x18\x08 \x01(\x05\x12\t\n\x01v\x18\t \x01(\x05\"\x97\x01\n\x11SDK3PushLogXiadan\x12\"\n\x02\x64i\x18\x01 \x01(\x0b\x32\x16.SDK3PushLogDeviceInfo\x12\r\n\x05\x61ppid\x18\x02 \x01(\t\x12\n\n\x02os\x18\x03 \x01(\t\x12\x0b\n\x03uid\x18\x04 \x01(\t\x12\x0b\n\x03rid\x18\x05 \x01(\t\x12\x0b\n\x03sid\x18\x06 \x01(\t\x12\r\n\x05money\x18\x07 \x01(\x05\x12\r\n\x05\x63poid\x18\x08 \x01(\tBC\xca\x02\x1cmodules\\collect\\parse_app\\pb\xe2\x02!modules\\collect\\parse_app\\pb_metab\x06proto3')
)




_SDK3PUSHLOGDEVICEINFO = _descriptor.Descriptor(
  name='SDK3PushLogDeviceInfo',
  full_name='SDK3PushLogDeviceInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='adId', full_name='SDK3PushLogDeviceInfo.adId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='andId', full_name='SDK3PushLogDeviceInfo.andId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ch', full_name='SDK3PushLogDeviceInfo.ch', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dn', full_name='SDK3PushLogDeviceInfo.dn', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='did', full_name='SDK3PushLogDeviceInfo.did', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='imei', full_name='SDK3PushLogDeviceInfo.imei', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='net', full_name='SDK3PushLogDeviceInfo.net', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='osv', full_name='SDK3PushLogDeviceInfo.osv', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ss', full_name='SDK3PushLogDeviceInfo.ss', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sdkv', full_name='SDK3PushLogDeviceInfo.sdkv', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gv', full_name='SDK3PushLogDeviceInfo.gv', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='oaid', full_name='SDK3PushLogDeviceInfo.oaid', index=11,
      number=12, type=9, cpp_type=9, label=1,
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
  serialized_start=17,
  serialized_end=198,
)


_SDK3PUSHLOGUSERINFO = _descriptor.Descriptor(
  name='SDK3PushLogUserInfo',
  full_name='SDK3PushLogUserInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='level', full_name='SDK3PushLogUserInfo.level', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rid', full_name='SDK3PushLogUserInfo.rid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rn', full_name='SDK3PushLogUserInfo.rn', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sid', full_name='SDK3PushLogUserInfo.sid', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uid', full_name='SDK3PushLogUserInfo.uid', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=200,
  serialized_end=287,
)


_SDK3PUSHLOGSTART_AINFOENTRY = _descriptor.Descriptor(
  name='AinfoEntry',
  full_name='SDK3PushLogStart.AinfoEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='SDK3PushLogStart.AinfoEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='SDK3PushLogStart.AinfoEntry.value', index=1,
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
  serialized_start=448,
  serialized_end=492,
)

_SDK3PUSHLOGSTART = _descriptor.Descriptor(
  name='SDK3PushLogStart',
  full_name='SDK3PushLogStart',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='di', full_name='SDK3PushLogStart.di', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='appid', full_name='SDK3PushLogStart.appid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='os', full_name='SDK3PushLogStart.os', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pn', full_name='SDK3PushLogStart.pn', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packdate', full_name='SDK3PushLogStart.packdate', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ainfo', full_name='SDK3PushLogStart.ainfo', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SDK3PUSHLOGSTART_AINFOENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=290,
  serialized_end=492,
)


_SDK3PUSHLOGGAME = _descriptor.Descriptor(
  name='SDK3PushLogGame',
  full_name='SDK3PushLogGame',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='di', full_name='SDK3PushLogGame.di', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ui', full_name='SDK3PushLogGame.ui', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='appid', full_name='SDK3PushLogGame.appid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='os', full_name='SDK3PushLogGame.os', index=3,
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
  serialized_start=494,
  serialized_end=608,
)


_SDK3PUSHLOGROLEUPDATE = _descriptor.Descriptor(
  name='SDK3PushLogRoleUpdate',
  full_name='SDK3PushLogRoleUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='di', full_name='SDK3PushLogRoleUpdate.di', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ui', full_name='SDK3PushLogRoleUpdate.ui', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='appid', full_name='SDK3PushLogRoleUpdate.appid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='os', full_name='SDK3PushLogRoleUpdate.os', index=3,
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
  serialized_start=610,
  serialized_end=730,
)


_SDK3PUSHLOGDUR = _descriptor.Descriptor(
  name='SDK3PushLogDur',
  full_name='SDK3PushLogDur',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='di', full_name='SDK3PushLogDur.di', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='appid', full_name='SDK3PushLogDur.appid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='os', full_name='SDK3PushLogDur.os', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uid', full_name='SDK3PushLogDur.uid', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rid', full_name='SDK3PushLogDur.rid', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sid', full_name='SDK3PushLogDur.sid', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lifeid', full_name='SDK3PushLogDur.lifeid', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dur', full_name='SDK3PushLogDur.dur', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='st', full_name='SDK3PushLogDur.st', index=8,
      number=9, type=5, cpp_type=1, label=1,
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
  serialized_start=733,
  serialized_end=892,
)


_SDK3PUSHLOGPERIOD = _descriptor.Descriptor(
  name='SDK3PushLogPeriod',
  full_name='SDK3PushLogPeriod',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='di', full_name='SDK3PushLogPeriod.di', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='appid', full_name='SDK3PushLogPeriod.appid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='os', full_name='SDK3PushLogPeriod.os', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uid', full_name='SDK3PushLogPeriod.uid', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rid', full_name='SDK3PushLogPeriod.rid', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sid', full_name='SDK3PushLogPeriod.sid', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lifeid', full_name='SDK3PushLogPeriod.lifeid', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='period', full_name='SDK3PushLogPeriod.period', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='v', full_name='SDK3PushLogPeriod.v', index=8,
      number=9, type=5, cpp_type=1, label=1,
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
  serialized_start=895,
  serialized_end=1059,
)


_SDK3PUSHLOGXIADAN = _descriptor.Descriptor(
  name='SDK3PushLogXiadan',
  full_name='SDK3PushLogXiadan',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='di', full_name='SDK3PushLogXiadan.di', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='appid', full_name='SDK3PushLogXiadan.appid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='os', full_name='SDK3PushLogXiadan.os', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uid', full_name='SDK3PushLogXiadan.uid', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rid', full_name='SDK3PushLogXiadan.rid', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sid', full_name='SDK3PushLogXiadan.sid', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='money', full_name='SDK3PushLogXiadan.money', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cpoid', full_name='SDK3PushLogXiadan.cpoid', index=7,
      number=8, type=9, cpp_type=9, label=1,
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
  serialized_start=1062,
  serialized_end=1213,
)

_SDK3PUSHLOGSTART_AINFOENTRY.containing_type = _SDK3PUSHLOGSTART
_SDK3PUSHLOGSTART.fields_by_name['di'].message_type = _SDK3PUSHLOGDEVICEINFO
_SDK3PUSHLOGSTART.fields_by_name['ainfo'].message_type = _SDK3PUSHLOGSTART_AINFOENTRY
_SDK3PUSHLOGGAME.fields_by_name['di'].message_type = _SDK3PUSHLOGDEVICEINFO
_SDK3PUSHLOGGAME.fields_by_name['ui'].message_type = _SDK3PUSHLOGUSERINFO
_SDK3PUSHLOGROLEUPDATE.fields_by_name['di'].message_type = _SDK3PUSHLOGDEVICEINFO
_SDK3PUSHLOGROLEUPDATE.fields_by_name['ui'].message_type = _SDK3PUSHLOGUSERINFO
_SDK3PUSHLOGDUR.fields_by_name['di'].message_type = _SDK3PUSHLOGDEVICEINFO
_SDK3PUSHLOGPERIOD.fields_by_name['di'].message_type = _SDK3PUSHLOGDEVICEINFO
_SDK3PUSHLOGXIADAN.fields_by_name['di'].message_type = _SDK3PUSHLOGDEVICEINFO
DESCRIPTOR.message_types_by_name['SDK3PushLogDeviceInfo'] = _SDK3PUSHLOGDEVICEINFO
DESCRIPTOR.message_types_by_name['SDK3PushLogUserInfo'] = _SDK3PUSHLOGUSERINFO
DESCRIPTOR.message_types_by_name['SDK3PushLogStart'] = _SDK3PUSHLOGSTART
DESCRIPTOR.message_types_by_name['SDK3PushLogGame'] = _SDK3PUSHLOGGAME
DESCRIPTOR.message_types_by_name['SDK3PushLogRoleUpdate'] = _SDK3PUSHLOGROLEUPDATE
DESCRIPTOR.message_types_by_name['SDK3PushLogDur'] = _SDK3PUSHLOGDUR
DESCRIPTOR.message_types_by_name['SDK3PushLogPeriod'] = _SDK3PUSHLOGPERIOD
DESCRIPTOR.message_types_by_name['SDK3PushLogXiadan'] = _SDK3PUSHLOGXIADAN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SDK3PushLogDeviceInfo = _reflection.GeneratedProtocolMessageType('SDK3PushLogDeviceInfo', (_message.Message,), dict(
  DESCRIPTOR = _SDK3PUSHLOGDEVICEINFO,
  __module__ = 'bn_sdk_pb2'
  # @@protoc_insertion_point(class_scope:SDK3PushLogDeviceInfo)
  ))
_sym_db.RegisterMessage(SDK3PushLogDeviceInfo)

SDK3PushLogUserInfo = _reflection.GeneratedProtocolMessageType('SDK3PushLogUserInfo', (_message.Message,), dict(
  DESCRIPTOR = _SDK3PUSHLOGUSERINFO,
  __module__ = 'bn_sdk_pb2'
  # @@protoc_insertion_point(class_scope:SDK3PushLogUserInfo)
  ))
_sym_db.RegisterMessage(SDK3PushLogUserInfo)

SDK3PushLogStart = _reflection.GeneratedProtocolMessageType('SDK3PushLogStart', (_message.Message,), dict(

  AinfoEntry = _reflection.GeneratedProtocolMessageType('AinfoEntry', (_message.Message,), dict(
    DESCRIPTOR = _SDK3PUSHLOGSTART_AINFOENTRY,
    __module__ = 'bn_sdk_pb2'
    # @@protoc_insertion_point(class_scope:SDK3PushLogStart.AinfoEntry)
    ))
  ,
  DESCRIPTOR = _SDK3PUSHLOGSTART,
  __module__ = 'bn_sdk_pb2'
  # @@protoc_insertion_point(class_scope:SDK3PushLogStart)
  ))
_sym_db.RegisterMessage(SDK3PushLogStart)
_sym_db.RegisterMessage(SDK3PushLogStart.AinfoEntry)

SDK3PushLogGame = _reflection.GeneratedProtocolMessageType('SDK3PushLogGame', (_message.Message,), dict(
  DESCRIPTOR = _SDK3PUSHLOGGAME,
  __module__ = 'bn_sdk_pb2'
  # @@protoc_insertion_point(class_scope:SDK3PushLogGame)
  ))
_sym_db.RegisterMessage(SDK3PushLogGame)

SDK3PushLogRoleUpdate = _reflection.GeneratedProtocolMessageType('SDK3PushLogRoleUpdate', (_message.Message,), dict(
  DESCRIPTOR = _SDK3PUSHLOGROLEUPDATE,
  __module__ = 'bn_sdk_pb2'
  # @@protoc_insertion_point(class_scope:SDK3PushLogRoleUpdate)
  ))
_sym_db.RegisterMessage(SDK3PushLogRoleUpdate)

SDK3PushLogDur = _reflection.GeneratedProtocolMessageType('SDK3PushLogDur', (_message.Message,), dict(
  DESCRIPTOR = _SDK3PUSHLOGDUR,
  __module__ = 'bn_sdk_pb2'
  # @@protoc_insertion_point(class_scope:SDK3PushLogDur)
  ))
_sym_db.RegisterMessage(SDK3PushLogDur)

SDK3PushLogPeriod = _reflection.GeneratedProtocolMessageType('SDK3PushLogPeriod', (_message.Message,), dict(
  DESCRIPTOR = _SDK3PUSHLOGPERIOD,
  __module__ = 'bn_sdk_pb2'
  # @@protoc_insertion_point(class_scope:SDK3PushLogPeriod)
  ))
_sym_db.RegisterMessage(SDK3PushLogPeriod)

SDK3PushLogXiadan = _reflection.GeneratedProtocolMessageType('SDK3PushLogXiadan', (_message.Message,), dict(
  DESCRIPTOR = _SDK3PUSHLOGXIADAN,
  __module__ = 'bn_sdk_pb2'
  # @@protoc_insertion_point(class_scope:SDK3PushLogXiadan)
  ))
_sym_db.RegisterMessage(SDK3PushLogXiadan)


DESCRIPTOR._options = None
_SDK3PUSHLOGSTART_AINFOENTRY._options = None
# @@protoc_insertion_point(module_scope)

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sms.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sms.proto',
  package='wlst.ws',
  syntax='proto3',
  serialized_pb=_b('\n\tsms.proto\x12\x07wlst.ws\"\xfe\x01\n\x04Head\x12\x0b\n\x03idx\x18\x01 \x01(\x03\x12\x0b\n\x03ver\x18\x02 \x01(\x05\x12\x0f\n\x07if_name\x18\x03 \x01(\t\x12\x0e\n\x06unique\x18\x05 \x01(\t\x12\r\n\x05if_dt\x18\x64 \x01(\x03\x12\r\n\x05if_st\x18\x65 \x01(\x05\x12\x0e\n\x06if_msg\x18\x66 \x01(\t\x12\x12\n\nmsg_filter\x18g \x03(\t\x12\x13\n\npaging_num\x18\xc8\x01 \x01(\x05\x12\x13\n\npaging_idx\x18\xc9\x01 \x01(\x05\x12\x15\n\x0cpaging_total\x18\xca\x01 \x01(\x05\x12\x1a\n\x11paging_buffer_tag\x18\xcb\x01 \x01(\x03\x12\x1c\n\x13paging_record_total\x18\xcc\x01 \x01(\x05\"&\n\x07\x43ommAns\x12\x1b\n\x04head\x18\x01 \x01(\x0b\x32\r.wlst.ws.Head\"A\n\x0frqQuerySmsAlarm\x12\x1b\n\x04head\x18\x01 \x01(\x0b\x32\r.wlst.ws.Head\x12\x11\n\tdata_mark\x18\x02 \x01(\x05\"\x92\x02\n\rQuerySmsAlarm\x12\x1b\n\x04head\x18\x01 \x01(\x0b\x32\r.wlst.ws.Head\x12\x32\n\tsms_alarm\x18\x03 \x03(\x0b\x32\x1f.wlst.ws.QuerySmsAlarm.SmsAlarm\x1a\xaf\x01\n\x08SmsAlarm\x12\x11\n\tdata_mark\x18\x01 \x01(\x05\x12\x11\n\trecord_id\x18\x02 \x01(\x03\x12\x0e\n\x06tml_id\x18\x03 \x01(\x03\x12\x10\n\x08tml_name\x18\x04 \x01(\t\x12\x0f\n\x07loop_id\x18\x05 \x01(\x05\x12\x11\n\tloop_name\x18\x06 \x01(\t\x12\x12\n\nfault_name\x18\x07 \x01(\t\x12\x10\n\x08user_tel\x18\x08 \x01(\x03\x12\x11\n\tdt_create\x18\t \x01(\x03\"i\n\x0eUpdateSmsAlarm\x12\x1b\n\x04head\x18\x01 \x01(\x0b\x32\r.wlst.ws.Head\x12\x15\n\trecord_id\x18\x02 \x03(\x05\x42\x02\x10\x01\x12\x10\n\x08user_tel\x18\x03 \x01(\x03\x12\x11\n\tfault_msg\x18\x04 \x01(\t\"<\n\nrqUserInfo\x12\x1b\n\x04head\x18\x01 \x01(\x0b\x32\r.wlst.ws.Head\x12\x11\n\tuser_name\x18\x02 \x01(\t\"}\n\x08UserInfo\x12\x1b\n\x04head\x18\x01 \x01(\x0b\x32\r.wlst.ws.Head\x12-\n\tuser_view\x18\x02 \x03(\x0b\x32\x1a.wlst.ws.UserInfo.UserView\x1a%\n\x08UserView\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x0b\n\x03tel\x18\x05 \x01(\tB\x02H\x01\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_HEAD = _descriptor.Descriptor(
  name='Head',
  full_name='wlst.ws.Head',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='idx', full_name='wlst.ws.Head.idx', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ver', full_name='wlst.ws.Head.ver', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='if_name', full_name='wlst.ws.Head.if_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unique', full_name='wlst.ws.Head.unique', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='if_dt', full_name='wlst.ws.Head.if_dt', index=4,
      number=100, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='if_st', full_name='wlst.ws.Head.if_st', index=5,
      number=101, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='if_msg', full_name='wlst.ws.Head.if_msg', index=6,
      number=102, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msg_filter', full_name='wlst.ws.Head.msg_filter', index=7,
      number=103, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='paging_num', full_name='wlst.ws.Head.paging_num', index=8,
      number=200, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='paging_idx', full_name='wlst.ws.Head.paging_idx', index=9,
      number=201, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='paging_total', full_name='wlst.ws.Head.paging_total', index=10,
      number=202, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='paging_buffer_tag', full_name='wlst.ws.Head.paging_buffer_tag', index=11,
      number=203, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='paging_record_total', full_name='wlst.ws.Head.paging_record_total', index=12,
      number=204, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=23,
  serialized_end=277,
)


_COMMANS = _descriptor.Descriptor(
  name='CommAns',
  full_name='wlst.ws.CommAns',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='head', full_name='wlst.ws.CommAns.head', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=279,
  serialized_end=317,
)


_RQQUERYSMSALARM = _descriptor.Descriptor(
  name='rqQuerySmsAlarm',
  full_name='wlst.ws.rqQuerySmsAlarm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='head', full_name='wlst.ws.rqQuerySmsAlarm.head', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data_mark', full_name='wlst.ws.rqQuerySmsAlarm.data_mark', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=319,
  serialized_end=384,
)


_QUERYSMSALARM_SMSALARM = _descriptor.Descriptor(
  name='SmsAlarm',
  full_name='wlst.ws.QuerySmsAlarm.SmsAlarm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data_mark', full_name='wlst.ws.QuerySmsAlarm.SmsAlarm.data_mark', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='record_id', full_name='wlst.ws.QuerySmsAlarm.SmsAlarm.record_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tml_id', full_name='wlst.ws.QuerySmsAlarm.SmsAlarm.tml_id', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tml_name', full_name='wlst.ws.QuerySmsAlarm.SmsAlarm.tml_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='loop_id', full_name='wlst.ws.QuerySmsAlarm.SmsAlarm.loop_id', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='loop_name', full_name='wlst.ws.QuerySmsAlarm.SmsAlarm.loop_name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fault_name', full_name='wlst.ws.QuerySmsAlarm.SmsAlarm.fault_name', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_tel', full_name='wlst.ws.QuerySmsAlarm.SmsAlarm.user_tel', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dt_create', full_name='wlst.ws.QuerySmsAlarm.SmsAlarm.dt_create', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=486,
  serialized_end=661,
)

_QUERYSMSALARM = _descriptor.Descriptor(
  name='QuerySmsAlarm',
  full_name='wlst.ws.QuerySmsAlarm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='head', full_name='wlst.ws.QuerySmsAlarm.head', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sms_alarm', full_name='wlst.ws.QuerySmsAlarm.sms_alarm', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_QUERYSMSALARM_SMSALARM, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=387,
  serialized_end=661,
)


_UPDATESMSALARM = _descriptor.Descriptor(
  name='UpdateSmsAlarm',
  full_name='wlst.ws.UpdateSmsAlarm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='head', full_name='wlst.ws.UpdateSmsAlarm.head', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='record_id', full_name='wlst.ws.UpdateSmsAlarm.record_id', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
    _descriptor.FieldDescriptor(
      name='user_tel', full_name='wlst.ws.UpdateSmsAlarm.user_tel', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fault_msg', full_name='wlst.ws.UpdateSmsAlarm.fault_msg', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=663,
  serialized_end=768,
)


_RQUSERINFO = _descriptor.Descriptor(
  name='rqUserInfo',
  full_name='wlst.ws.rqUserInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='head', full_name='wlst.ws.rqUserInfo.head', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_name', full_name='wlst.ws.rqUserInfo.user_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=770,
  serialized_end=830,
)


_USERINFO_USERVIEW = _descriptor.Descriptor(
  name='UserView',
  full_name='wlst.ws.UserInfo.UserView',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='wlst.ws.UserInfo.UserView.user', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tel', full_name='wlst.ws.UserInfo.UserView.tel', index=1,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=920,
  serialized_end=957,
)

_USERINFO = _descriptor.Descriptor(
  name='UserInfo',
  full_name='wlst.ws.UserInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='head', full_name='wlst.ws.UserInfo.head', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_view', full_name='wlst.ws.UserInfo.user_view', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_USERINFO_USERVIEW, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=832,
  serialized_end=957,
)

_COMMANS.fields_by_name['head'].message_type = _HEAD
_RQQUERYSMSALARM.fields_by_name['head'].message_type = _HEAD
_QUERYSMSALARM_SMSALARM.containing_type = _QUERYSMSALARM
_QUERYSMSALARM.fields_by_name['head'].message_type = _HEAD
_QUERYSMSALARM.fields_by_name['sms_alarm'].message_type = _QUERYSMSALARM_SMSALARM
_UPDATESMSALARM.fields_by_name['head'].message_type = _HEAD
_RQUSERINFO.fields_by_name['head'].message_type = _HEAD
_USERINFO_USERVIEW.containing_type = _USERINFO
_USERINFO.fields_by_name['head'].message_type = _HEAD
_USERINFO.fields_by_name['user_view'].message_type = _USERINFO_USERVIEW
DESCRIPTOR.message_types_by_name['Head'] = _HEAD
DESCRIPTOR.message_types_by_name['CommAns'] = _COMMANS
DESCRIPTOR.message_types_by_name['rqQuerySmsAlarm'] = _RQQUERYSMSALARM
DESCRIPTOR.message_types_by_name['QuerySmsAlarm'] = _QUERYSMSALARM
DESCRIPTOR.message_types_by_name['UpdateSmsAlarm'] = _UPDATESMSALARM
DESCRIPTOR.message_types_by_name['rqUserInfo'] = _RQUSERINFO
DESCRIPTOR.message_types_by_name['UserInfo'] = _USERINFO

Head = _reflection.GeneratedProtocolMessageType('Head', (_message.Message,), dict(
  DESCRIPTOR = _HEAD,
  __module__ = 'sms_pb2'
  # @@protoc_insertion_point(class_scope:wlst.ws.Head)
  ))
_sym_db.RegisterMessage(Head)

CommAns = _reflection.GeneratedProtocolMessageType('CommAns', (_message.Message,), dict(
  DESCRIPTOR = _COMMANS,
  __module__ = 'sms_pb2'
  # @@protoc_insertion_point(class_scope:wlst.ws.CommAns)
  ))
_sym_db.RegisterMessage(CommAns)

rqQuerySmsAlarm = _reflection.GeneratedProtocolMessageType('rqQuerySmsAlarm', (_message.Message,), dict(
  DESCRIPTOR = _RQQUERYSMSALARM,
  __module__ = 'sms_pb2'
  # @@protoc_insertion_point(class_scope:wlst.ws.rqQuerySmsAlarm)
  ))
_sym_db.RegisterMessage(rqQuerySmsAlarm)

QuerySmsAlarm = _reflection.GeneratedProtocolMessageType('QuerySmsAlarm', (_message.Message,), dict(

  SmsAlarm = _reflection.GeneratedProtocolMessageType('SmsAlarm', (_message.Message,), dict(
    DESCRIPTOR = _QUERYSMSALARM_SMSALARM,
    __module__ = 'sms_pb2'
    # @@protoc_insertion_point(class_scope:wlst.ws.QuerySmsAlarm.SmsAlarm)
    ))
  ,
  DESCRIPTOR = _QUERYSMSALARM,
  __module__ = 'sms_pb2'
  # @@protoc_insertion_point(class_scope:wlst.ws.QuerySmsAlarm)
  ))
_sym_db.RegisterMessage(QuerySmsAlarm)
_sym_db.RegisterMessage(QuerySmsAlarm.SmsAlarm)

UpdateSmsAlarm = _reflection.GeneratedProtocolMessageType('UpdateSmsAlarm', (_message.Message,), dict(
  DESCRIPTOR = _UPDATESMSALARM,
  __module__ = 'sms_pb2'
  # @@protoc_insertion_point(class_scope:wlst.ws.UpdateSmsAlarm)
  ))
_sym_db.RegisterMessage(UpdateSmsAlarm)

rqUserInfo = _reflection.GeneratedProtocolMessageType('rqUserInfo', (_message.Message,), dict(
  DESCRIPTOR = _RQUSERINFO,
  __module__ = 'sms_pb2'
  # @@protoc_insertion_point(class_scope:wlst.ws.rqUserInfo)
  ))
_sym_db.RegisterMessage(rqUserInfo)

UserInfo = _reflection.GeneratedProtocolMessageType('UserInfo', (_message.Message,), dict(

  UserView = _reflection.GeneratedProtocolMessageType('UserView', (_message.Message,), dict(
    DESCRIPTOR = _USERINFO_USERVIEW,
    __module__ = 'sms_pb2'
    # @@protoc_insertion_point(class_scope:wlst.ws.UserInfo.UserView)
    ))
  ,
  DESCRIPTOR = _USERINFO,
  __module__ = 'sms_pb2'
  # @@protoc_insertion_point(class_scope:wlst.ws.UserInfo)
  ))
_sym_db.RegisterMessage(UserInfo)
_sym_db.RegisterMessage(UserInfo.UserView)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\001'))
_UPDATESMSALARM.fields_by_name['record_id'].has_options = True
_UPDATESMSALARM.fields_by_name['record_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
# @@protoc_insertion_point(module_scope)
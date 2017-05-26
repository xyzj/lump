# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: msg_with_ctrl.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import protocol_head_pb2 as protocol__head__pb2
import protocol_tml_pb2 as protocol__tml__pb2
import protocol_tp_pb2 as protocol__tp__pb2
import protocol_3c_pb2 as protocol__3c__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='msg_with_ctrl.proto',
  package='wlst.pb2',
  syntax='proto3',
  serialized_pb=_b('\n\x13msg_with_ctrl.proto\x12\x08wlst.pb2\x1a\x13protocol_head.proto\x1a\x12protocol_tml.proto\x1a\x11protocol_tp.proto\x1a\x11protocol_3c.proto\"\xb3\x03\n\x0bMsgWithCtrl\x12\x1c\n\x04head\x18\x01 \x01(\x0b\x32\x0e.wlst.pb2.Head\x12\x1c\n\x04\x61rgs\x18\x02 \x01(\x0b\x32\x0e.wlst.pb2.Args\x12&\n\x07syscmds\x18\x03 \x01(\x0b\x32\x15.wlst.pb2.SysCommands\x12(\n\x08wlst_tml\x18\x64 \x01(\x0b\x32\x16.wlst.pb2.WlstTerminal\x12/\n\rwlst_com_0000\x18\xe8\x07 \x01(\x0b\x32\x17.wlst.pb2.Wlst_com_0000\x12/\n\rwlst_com_3e01\x18\xe9\x07 \x01(\x0b\x32\x17.wlst.pb2.Wlst_com_3e01\x12/\n\rwlst_com_3e02\x18\xea\x07 \x01(\x0b\x32\x17.wlst.pb2.Wlst_com_3e02\x12/\n\rwlst_com_3e82\x18\xeb\x07 \x01(\x0b\x32\x17.wlst.pb2.Wlst_com_3e82\x12/\n\rwlst_com_3e81\x18\xec\x07 \x01(\x0b\x32\x17.wlst.pb2.Wlst_com_3e02\x12!\n\x08wxjy_esu\x18\xd0\x0f \x01(\x0b\x32\x0e.wlst.pb2.Wxjy\"\xf0\x01\n\x0bSubmitAlarm\x12\x33\n\nalarm_view\x18\x02 \x03(\x0b\x32\x1f.wlst.pb2.SubmitAlarm.AlarmView\x1a\xab\x01\n\tAlarmView\x12\x11\n\tdt_create\x18\x01 \x01(\x03\x12\x0e\n\x06\x65rr_id\x18\x02 \x01(\x05\x12\x0e\n\x06tml_id\x18\x03 \x01(\x05\x12\x0f\n\x07loop_id\x18\x04 \x01(\x05\x12\x0f\n\x07lamp_id\x18\x05 \x01(\x05\x12\x11\n\terr_count\x18\x06 \x01(\x05\x12\x11\n\tdt_remove\x18\x08 \x01(\x03\x12\x10\n\x08is_alarm\x18\t \x01(\x05\x12\x11\n\talarm_src\x18\n \x01(\x05\x42\x02H\x01\x62\x06proto3')
  ,
  dependencies=[protocol__head__pb2.DESCRIPTOR,protocol__tml__pb2.DESCRIPTOR,protocol__tp__pb2.DESCRIPTOR,protocol__3c__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_MSGWITHCTRL = _descriptor.Descriptor(
  name='MsgWithCtrl',
  full_name='wlst.pb2.MsgWithCtrl',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='head', full_name='wlst.pb2.MsgWithCtrl.head', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='args', full_name='wlst.pb2.MsgWithCtrl.args', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='syscmds', full_name='wlst.pb2.MsgWithCtrl.syscmds', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wlst_tml', full_name='wlst.pb2.MsgWithCtrl.wlst_tml', index=3,
      number=100, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wlst_com_0000', full_name='wlst.pb2.MsgWithCtrl.wlst_com_0000', index=4,
      number=1000, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wlst_com_3e01', full_name='wlst.pb2.MsgWithCtrl.wlst_com_3e01', index=5,
      number=1001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wlst_com_3e02', full_name='wlst.pb2.MsgWithCtrl.wlst_com_3e02', index=6,
      number=1002, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wlst_com_3e82', full_name='wlst.pb2.MsgWithCtrl.wlst_com_3e82', index=7,
      number=1003, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wlst_com_3e81', full_name='wlst.pb2.MsgWithCtrl.wlst_com_3e81', index=8,
      number=1004, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wxjy_esu', full_name='wlst.pb2.MsgWithCtrl.wxjy_esu', index=9,
      number=2000, type=11, cpp_type=10, label=1,
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
  serialized_start=113,
  serialized_end=548,
)


_SUBMITALARM_ALARMVIEW = _descriptor.Descriptor(
  name='AlarmView',
  full_name='wlst.pb2.SubmitAlarm.AlarmView',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dt_create', full_name='wlst.pb2.SubmitAlarm.AlarmView.dt_create', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='err_id', full_name='wlst.pb2.SubmitAlarm.AlarmView.err_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tml_id', full_name='wlst.pb2.SubmitAlarm.AlarmView.tml_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='loop_id', full_name='wlst.pb2.SubmitAlarm.AlarmView.loop_id', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lamp_id', full_name='wlst.pb2.SubmitAlarm.AlarmView.lamp_id', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='err_count', full_name='wlst.pb2.SubmitAlarm.AlarmView.err_count', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dt_remove', full_name='wlst.pb2.SubmitAlarm.AlarmView.dt_remove', index=6,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_alarm', full_name='wlst.pb2.SubmitAlarm.AlarmView.is_alarm', index=7,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='alarm_src', full_name='wlst.pb2.SubmitAlarm.AlarmView.alarm_src', index=8,
      number=10, type=5, cpp_type=1, label=1,
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
  serialized_start=620,
  serialized_end=791,
)

_SUBMITALARM = _descriptor.Descriptor(
  name='SubmitAlarm',
  full_name='wlst.pb2.SubmitAlarm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='alarm_view', full_name='wlst.pb2.SubmitAlarm.alarm_view', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_SUBMITALARM_ALARMVIEW, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=551,
  serialized_end=791,
)

_MSGWITHCTRL.fields_by_name['head'].message_type = protocol__head__pb2._HEAD
_MSGWITHCTRL.fields_by_name['args'].message_type = protocol__head__pb2._ARGS
_MSGWITHCTRL.fields_by_name['syscmds'].message_type = protocol__head__pb2._SYSCOMMANDS
_MSGWITHCTRL.fields_by_name['wlst_tml'].message_type = protocol__tml__pb2._WLSTTERMINAL
_MSGWITHCTRL.fields_by_name['wlst_com_0000'].message_type = protocol__3c__pb2._WLST_COM_0000
_MSGWITHCTRL.fields_by_name['wlst_com_3e01'].message_type = protocol__3c__pb2._WLST_COM_3E01
_MSGWITHCTRL.fields_by_name['wlst_com_3e02'].message_type = protocol__3c__pb2._WLST_COM_3E02
_MSGWITHCTRL.fields_by_name['wlst_com_3e82'].message_type = protocol__3c__pb2._WLST_COM_3E82
_MSGWITHCTRL.fields_by_name['wlst_com_3e81'].message_type = protocol__3c__pb2._WLST_COM_3E02
_MSGWITHCTRL.fields_by_name['wxjy_esu'].message_type = protocol__tp__pb2._WXJY
_SUBMITALARM_ALARMVIEW.containing_type = _SUBMITALARM
_SUBMITALARM.fields_by_name['alarm_view'].message_type = _SUBMITALARM_ALARMVIEW
DESCRIPTOR.message_types_by_name['MsgWithCtrl'] = _MSGWITHCTRL
DESCRIPTOR.message_types_by_name['SubmitAlarm'] = _SUBMITALARM

MsgWithCtrl = _reflection.GeneratedProtocolMessageType('MsgWithCtrl', (_message.Message,), dict(
  DESCRIPTOR = _MSGWITHCTRL,
  __module__ = 'msg_with_ctrl_pb2'
  # @@protoc_insertion_point(class_scope:wlst.pb2.MsgWithCtrl)
  ))
_sym_db.RegisterMessage(MsgWithCtrl)

SubmitAlarm = _reflection.GeneratedProtocolMessageType('SubmitAlarm', (_message.Message,), dict(

  AlarmView = _reflection.GeneratedProtocolMessageType('AlarmView', (_message.Message,), dict(
    DESCRIPTOR = _SUBMITALARM_ALARMVIEW,
    __module__ = 'msg_with_ctrl_pb2'
    # @@protoc_insertion_point(class_scope:wlst.pb2.SubmitAlarm.AlarmView)
    ))
  ,
  DESCRIPTOR = _SUBMITALARM,
  __module__ = 'msg_with_ctrl_pb2'
  # @@protoc_insertion_point(class_scope:wlst.pb2.SubmitAlarm)
  ))
_sym_db.RegisterMessage(SubmitAlarm)
_sym_db.RegisterMessage(SubmitAlarm.AlarmView)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\001'))
# @@protoc_insertion_point(module_scope)

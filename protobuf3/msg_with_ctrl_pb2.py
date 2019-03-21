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
  serialized_pb=_b('\n\x13msg_with_ctrl.proto\x12\x08wlst.pb2\x1a\x13protocol_head.proto\x1a\x12protocol_tml.proto\x1a\x11protocol_tp.proto\x1a\x11protocol_3c.proto\"\xe9\t\n\x0bMsgWithCtrl\x12\x1c\n\x04head\x18\x01 \x01(\x0b\x32\x0e.wlst.pb2.Head\x12\x1c\n\x04\x61rgs\x18\x02 \x01(\x0b\x32\x0e.wlst.pb2.Args\x12&\n\x07syscmds\x18\x03 \x01(\x0b\x32\x15.wlst.pb2.SysCommands\x12*\n\x0bPassthrough\x18\x63 \x01(\x0b\x32\x15.wlst.pb2.Passthrough\x12(\n\x08wlst_tml\x18\x64 \x01(\x0b\x32\x16.wlst.pb2.WlstTerminal\x12/\n\rwlst_com_0000\x18\xe8\x07 \x01(\x0b\x32\x17.wlst.pb2.Wlst_com_0000\x12/\n\rwlst_com_3e01\x18\xe9\x07 \x01(\x0b\x32\x17.wlst.pb2.Wlst_com_3e01\x12/\n\rwlst_com_3e02\x18\xea\x07 \x01(\x0b\x32\x17.wlst.pb2.Wlst_com_3e02\x12/\n\rwlst_com_3e82\x18\xeb\x07 \x01(\x0b\x32\x17.wlst.pb2.Wlst_com_3e82\x12/\n\rwlst_com_3e81\x18\xec\x07 \x01(\x0b\x32\x17.wlst.pb2.Wlst_com_3e02\x12/\n\rwlst_com_3e84\x18\xed\x07 \x01(\x0b\x32\x17.wlst.pb2.Wlst_com_3e84\x12/\n\rwxjy_esu_5500\x18\xd0\x0f \x01(\x0b\x32\x17.wlst.pb2.Wxjy_esu_5500\x12/\n\rwxjy_esu_d500\x18\xd1\x0f \x01(\x0b\x32\x17.wlst.pb2.Wxjy_esu_5500\x12/\n\rwxjy_esu_d700\x18\xd2\x0f \x01(\x0b\x32\x17.wlst.pb2.Wxjy_esu_d700\x12/\n\rwxjy_esu_d800\x18\xd3\x0f \x01(\x0b\x32\x17.wlst.pb2.Wxjy_esu_d800\x12/\n\rahhf_rtu_6804\x18\xb5\x10 \x01(\x0b\x32\x17.wlst.pb2.Ahhf_rtu_6804\x12/\n\rahhf_rtu_680a\x18\xb6\x10 \x01(\x0b\x32\x17.wlst.pb2.Ahhf_rtu_6804\x12-\n\x0c\x62lk_slu_6891\x18\x99\x11 \x01(\x0b\x32\x16.wlst.pb2.Blk_slu_6891\x12-\n\x0c\x62lk_slu_6892\x18\x9a\x11 \x01(\x0b\x32\x16.wlst.pb2.Blk_slu_6892\x12-\n\x0c\x62lk_slu_6887\x18\x9b\x11 \x01(\x0b\x32\x16.wlst.pb2.Blk_slu_6891\x12-\n\x0c\x62lk_slu_6888\x18\x9c\x11 \x01(\x0b\x32\x16.wlst.pb2.Blk_slu_6891\x12-\n\x0c\x62lk_slu_6895\x18\x9d\x11 \x01(\x0b\x32\x16.wlst.pb2.Blk_slu_6895\x12-\n\x0c\x62lk_slu_6896\x18\x9e\x11 \x01(\x0b\x32\x16.wlst.pb2.Blk_slu_6895\x12-\n\x0c\x62lk_slu_6889\x18\x9f\x11 \x01(\x0b\x32\x16.wlst.pb2.Blk_slu_6895\x12-\n\x0c\x62lk_slu_6890\x18\xa0\x11 \x01(\x0b\x32\x16.wlst.pb2.Blk_slu_6895\x12-\n\x0c\x62lk_slu_6893\x18\xa1\x11 \x01(\x0b\x32\x16.wlst.pb2.Blk_slu_6891\x12-\n\x0c\x62lk_slu_6894\x18\xa2\x11 \x01(\x0b\x32\x16.wlst.pb2.Blk_slu_6891\"\xa9\x02\n\x0bSubmitAlarm\x12\x33\n\nalarm_view\x18\x02 \x03(\x0b\x32\x1f.wlst.pb2.SubmitAlarm.AlarmView\x1a\xe4\x01\n\tAlarmView\x12\x11\n\tdt_create\x18\x01 \x01(\x03\x12\x0e\n\x06\x65rr_id\x18\x02 \x01(\x05\x12\x0e\n\x06tml_id\x18\x03 \x01(\x05\x12\x0f\n\x07loop_id\x18\x04 \x01(\x05\x12\x0f\n\x07lamp_id\x18\x05 \x01(\x05\x12\x11\n\terr_count\x18\x06 \x01(\x05\x12\x11\n\tdt_remove\x18\x08 \x01(\x03\x12\x10\n\x08is_alarm\x18\t \x01(\x05\x12\x11\n\talarm_src\x18\n \x01(\x05\x12\x12\n\nalarm_name\x18\x0b \x01(\t\x12\x10\n\x08tml_name\x18\x0c \x01(\t\x12\x11\n\tloop_name\x18\r \x01(\t\"?\n\x13SubmitSettingChange\x12\x14\n\x0csetting_type\x18\x01 \x01(\x05\x12\x12\n\x06tml_id\x18\x02 \x03(\x03\x42\x02\x10\x01\x42\x02H\x01\x62\x06proto3')
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
      name='Passthrough', full_name='wlst.pb2.MsgWithCtrl.Passthrough', index=3,
      number=99, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wlst_tml', full_name='wlst.pb2.MsgWithCtrl.wlst_tml', index=4,
      number=100, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wlst_com_0000', full_name='wlst.pb2.MsgWithCtrl.wlst_com_0000', index=5,
      number=1000, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wlst_com_3e01', full_name='wlst.pb2.MsgWithCtrl.wlst_com_3e01', index=6,
      number=1001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wlst_com_3e02', full_name='wlst.pb2.MsgWithCtrl.wlst_com_3e02', index=7,
      number=1002, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wlst_com_3e82', full_name='wlst.pb2.MsgWithCtrl.wlst_com_3e82', index=8,
      number=1003, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wlst_com_3e81', full_name='wlst.pb2.MsgWithCtrl.wlst_com_3e81', index=9,
      number=1004, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wlst_com_3e84', full_name='wlst.pb2.MsgWithCtrl.wlst_com_3e84', index=10,
      number=1005, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wxjy_esu_5500', full_name='wlst.pb2.MsgWithCtrl.wxjy_esu_5500', index=11,
      number=2000, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wxjy_esu_d500', full_name='wlst.pb2.MsgWithCtrl.wxjy_esu_d500', index=12,
      number=2001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wxjy_esu_d700', full_name='wlst.pb2.MsgWithCtrl.wxjy_esu_d700', index=13,
      number=2002, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wxjy_esu_d800', full_name='wlst.pb2.MsgWithCtrl.wxjy_esu_d800', index=14,
      number=2003, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ahhf_rtu_6804', full_name='wlst.pb2.MsgWithCtrl.ahhf_rtu_6804', index=15,
      number=2101, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ahhf_rtu_680a', full_name='wlst.pb2.MsgWithCtrl.ahhf_rtu_680a', index=16,
      number=2102, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='blk_slu_6891', full_name='wlst.pb2.MsgWithCtrl.blk_slu_6891', index=17,
      number=2201, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='blk_slu_6892', full_name='wlst.pb2.MsgWithCtrl.blk_slu_6892', index=18,
      number=2202, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='blk_slu_6887', full_name='wlst.pb2.MsgWithCtrl.blk_slu_6887', index=19,
      number=2203, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='blk_slu_6888', full_name='wlst.pb2.MsgWithCtrl.blk_slu_6888', index=20,
      number=2204, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='blk_slu_6895', full_name='wlst.pb2.MsgWithCtrl.blk_slu_6895', index=21,
      number=2205, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='blk_slu_6896', full_name='wlst.pb2.MsgWithCtrl.blk_slu_6896', index=22,
      number=2206, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='blk_slu_6889', full_name='wlst.pb2.MsgWithCtrl.blk_slu_6889', index=23,
      number=2207, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='blk_slu_6890', full_name='wlst.pb2.MsgWithCtrl.blk_slu_6890', index=24,
      number=2208, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='blk_slu_6893', full_name='wlst.pb2.MsgWithCtrl.blk_slu_6893', index=25,
      number=2209, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='blk_slu_6894', full_name='wlst.pb2.MsgWithCtrl.blk_slu_6894', index=26,
      number=2210, type=11, cpp_type=10, label=1,
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
  serialized_end=1370,
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
    _descriptor.FieldDescriptor(
      name='alarm_name', full_name='wlst.pb2.SubmitAlarm.AlarmView.alarm_name', index=9,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tml_name', full_name='wlst.pb2.SubmitAlarm.AlarmView.tml_name', index=10,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='loop_name', full_name='wlst.pb2.SubmitAlarm.AlarmView.loop_name', index=11,
      number=13, type=9, cpp_type=9, label=1,
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
  serialized_start=1442,
  serialized_end=1670,
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
  serialized_start=1373,
  serialized_end=1670,
)


_SUBMITSETTINGCHANGE = _descriptor.Descriptor(
  name='SubmitSettingChange',
  full_name='wlst.pb2.SubmitSettingChange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='setting_type', full_name='wlst.pb2.SubmitSettingChange.setting_type', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tml_id', full_name='wlst.pb2.SubmitSettingChange.tml_id', index=1,
      number=2, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
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
  serialized_start=1672,
  serialized_end=1735,
)

_MSGWITHCTRL.fields_by_name['head'].message_type = protocol__head__pb2._HEAD
_MSGWITHCTRL.fields_by_name['args'].message_type = protocol__head__pb2._ARGS
_MSGWITHCTRL.fields_by_name['syscmds'].message_type = protocol__head__pb2._SYSCOMMANDS
_MSGWITHCTRL.fields_by_name['Passthrough'].message_type = protocol__head__pb2._PASSTHROUGH
_MSGWITHCTRL.fields_by_name['wlst_tml'].message_type = protocol__tml__pb2._WLSTTERMINAL
_MSGWITHCTRL.fields_by_name['wlst_com_0000'].message_type = protocol__3c__pb2._WLST_COM_0000
_MSGWITHCTRL.fields_by_name['wlst_com_3e01'].message_type = protocol__3c__pb2._WLST_COM_3E01
_MSGWITHCTRL.fields_by_name['wlst_com_3e02'].message_type = protocol__3c__pb2._WLST_COM_3E02
_MSGWITHCTRL.fields_by_name['wlst_com_3e82'].message_type = protocol__3c__pb2._WLST_COM_3E82
_MSGWITHCTRL.fields_by_name['wlst_com_3e81'].message_type = protocol__3c__pb2._WLST_COM_3E02
_MSGWITHCTRL.fields_by_name['wlst_com_3e84'].message_type = protocol__3c__pb2._WLST_COM_3E84
_MSGWITHCTRL.fields_by_name['wxjy_esu_5500'].message_type = protocol__tp__pb2._WXJY_ESU_5500
_MSGWITHCTRL.fields_by_name['wxjy_esu_d500'].message_type = protocol__tp__pb2._WXJY_ESU_5500
_MSGWITHCTRL.fields_by_name['wxjy_esu_d700'].message_type = protocol__tp__pb2._WXJY_ESU_D700
_MSGWITHCTRL.fields_by_name['wxjy_esu_d800'].message_type = protocol__tp__pb2._WXJY_ESU_D800
_MSGWITHCTRL.fields_by_name['ahhf_rtu_6804'].message_type = protocol__tp__pb2._AHHF_RTU_6804
_MSGWITHCTRL.fields_by_name['ahhf_rtu_680a'].message_type = protocol__tp__pb2._AHHF_RTU_6804
_MSGWITHCTRL.fields_by_name['blk_slu_6891'].message_type = protocol__tp__pb2._BLK_SLU_6891
_MSGWITHCTRL.fields_by_name['blk_slu_6892'].message_type = protocol__tp__pb2._BLK_SLU_6892
_MSGWITHCTRL.fields_by_name['blk_slu_6887'].message_type = protocol__tp__pb2._BLK_SLU_6891
_MSGWITHCTRL.fields_by_name['blk_slu_6888'].message_type = protocol__tp__pb2._BLK_SLU_6891
_MSGWITHCTRL.fields_by_name['blk_slu_6895'].message_type = protocol__tp__pb2._BLK_SLU_6895
_MSGWITHCTRL.fields_by_name['blk_slu_6896'].message_type = protocol__tp__pb2._BLK_SLU_6895
_MSGWITHCTRL.fields_by_name['blk_slu_6889'].message_type = protocol__tp__pb2._BLK_SLU_6895
_MSGWITHCTRL.fields_by_name['blk_slu_6890'].message_type = protocol__tp__pb2._BLK_SLU_6895
_MSGWITHCTRL.fields_by_name['blk_slu_6893'].message_type = protocol__tp__pb2._BLK_SLU_6891
_MSGWITHCTRL.fields_by_name['blk_slu_6894'].message_type = protocol__tp__pb2._BLK_SLU_6891
_SUBMITALARM_ALARMVIEW.containing_type = _SUBMITALARM
_SUBMITALARM.fields_by_name['alarm_view'].message_type = _SUBMITALARM_ALARMVIEW
DESCRIPTOR.message_types_by_name['MsgWithCtrl'] = _MSGWITHCTRL
DESCRIPTOR.message_types_by_name['SubmitAlarm'] = _SUBMITALARM
DESCRIPTOR.message_types_by_name['SubmitSettingChange'] = _SUBMITSETTINGCHANGE

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

SubmitSettingChange = _reflection.GeneratedProtocolMessageType('SubmitSettingChange', (_message.Message,), dict(
  DESCRIPTOR = _SUBMITSETTINGCHANGE,
  __module__ = 'msg_with_ctrl_pb2'
  # @@protoc_insertion_point(class_scope:wlst.pb2.SubmitSettingChange)
  ))
_sym_db.RegisterMessage(SubmitSettingChange)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\001'))
_SUBMITSETTINGCHANGE.fields_by_name['tml_id'].has_options = True
_SUBMITSETTINGCHANGE.fields_by_name['tml_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
# @@protoc_insertion_point(module_scope)

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cr_ans.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='cr_ans.proto',
  package='protocol',
  serialized_pb='\n\x0c\x63r_ans.proto\x12\x08protocol\"4\n\x0c\x63hatroom_ans\x12\x10\n\x08\x61ns_type\x18\x01 \x01(\t\x12\x12\n\nans_result\x18\x02 \x01(\x05')




_CHATROOM_ANS = _descriptor.Descriptor(
  name='chatroom_ans',
  full_name='protocol.chatroom_ans',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ans_type', full_name='protocol.chatroom_ans.ans_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ans_result', full_name='protocol.chatroom_ans.ans_result', index=1,
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
  extension_ranges=[],
  serialized_start=26,
  serialized_end=78,
)

DESCRIPTOR.message_types_by_name['chatroom_ans'] = _CHATROOM_ANS

class chatroom_ans(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CHATROOM_ANS

  # @@protoc_insertion_point(class_scope:protocol.chatroom_ans)


# @@protoc_insertion_point(module_scope)

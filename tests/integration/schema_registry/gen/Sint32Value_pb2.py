# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Sint32Value.proto

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
  name='Sint32Value.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x11Sint32Value.proto\"\x1c\n\x0bSInt32Value\x12\r\n\x05value\x18\x01 \x01(\x11\x42.\n,io.confluent.kafka.serializers.protobuf.testb\x06proto3')
)




_SINT32VALUE = _descriptor.Descriptor(
  name='SInt32Value',
  full_name='SInt32Value',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='SInt32Value.value', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=21,
  serialized_end=49,
)

DESCRIPTOR.message_types_by_name['SInt32Value'] = _SINT32VALUE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SInt32Value = _reflection.GeneratedProtocolMessageType('SInt32Value', (_message.Message,), dict(
  DESCRIPTOR = _SINT32VALUE,
  __module__ = 'Sint32Value_pb2'
  # @@protoc_insertion_point(class_scope:SInt32Value)
  ))
_sym_db.RegisterMessage(SInt32Value)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n,io.confluent.kafka.serializers.protobuf.test'))
# @@protoc_insertion_point(module_scope)

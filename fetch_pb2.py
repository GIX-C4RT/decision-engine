# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fetch.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='fetch.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0b\x66\x65tch.proto\"P\n\x0f\x43heckOutRequest\x12\x0e\n\x06kit_ID\x18\x01 \x01(\x05\x12\x14\n\x0ckit_location\x18\x02 \x01(\x05\x12\x17\n\x0ftarget_location\x18\x03 \x01(\x05\"O\n\x0e\x43heckInRequest\x12\x0e\n\x06kit_ID\x18\x01 \x01(\x05\x12\x14\n\x0ckit_location\x18\x02 \x01(\x05\x12\x17\n\x0ftarget_location\x18\x03 \x01(\x05\"\"\n\rCheckOutReply\x12\x11\n\tdelivered\x18\x01 \x01(\x08\" \n\x0c\x43heckInReply\x12\x10\n\x08returned\x18\x01 \x01(\x08\x32\x64\n\x05\x46\x65tch\x12.\n\x08\x43heckOut\x12\x10.CheckOutRequest\x1a\x0e.CheckOutReply\"\x00\x12+\n\x07\x43heckIn\x12\x0f.CheckInRequest\x1a\r.CheckInReply\"\x00\x62\x06proto3'
)




_CHECKOUTREQUEST = _descriptor.Descriptor(
  name='CheckOutRequest',
  full_name='CheckOutRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='kit_ID', full_name='CheckOutRequest.kit_ID', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='kit_location', full_name='CheckOutRequest.kit_location', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target_location', full_name='CheckOutRequest.target_location', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=15,
  serialized_end=95,
)


_CHECKINREQUEST = _descriptor.Descriptor(
  name='CheckInRequest',
  full_name='CheckInRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='kit_ID', full_name='CheckInRequest.kit_ID', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='kit_location', full_name='CheckInRequest.kit_location', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target_location', full_name='CheckInRequest.target_location', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=97,
  serialized_end=176,
)


_CHECKOUTREPLY = _descriptor.Descriptor(
  name='CheckOutReply',
  full_name='CheckOutReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='delivered', full_name='CheckOutReply.delivered', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=178,
  serialized_end=212,
)


_CHECKINREPLY = _descriptor.Descriptor(
  name='CheckInReply',
  full_name='CheckInReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='returned', full_name='CheckInReply.returned', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=214,
  serialized_end=246,
)

DESCRIPTOR.message_types_by_name['CheckOutRequest'] = _CHECKOUTREQUEST
DESCRIPTOR.message_types_by_name['CheckInRequest'] = _CHECKINREQUEST
DESCRIPTOR.message_types_by_name['CheckOutReply'] = _CHECKOUTREPLY
DESCRIPTOR.message_types_by_name['CheckInReply'] = _CHECKINREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CheckOutRequest = _reflection.GeneratedProtocolMessageType('CheckOutRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHECKOUTREQUEST,
  '__module__' : 'fetch_pb2'
  # @@protoc_insertion_point(class_scope:CheckOutRequest)
  })
_sym_db.RegisterMessage(CheckOutRequest)

CheckInRequest = _reflection.GeneratedProtocolMessageType('CheckInRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHECKINREQUEST,
  '__module__' : 'fetch_pb2'
  # @@protoc_insertion_point(class_scope:CheckInRequest)
  })
_sym_db.RegisterMessage(CheckInRequest)

CheckOutReply = _reflection.GeneratedProtocolMessageType('CheckOutReply', (_message.Message,), {
  'DESCRIPTOR' : _CHECKOUTREPLY,
  '__module__' : 'fetch_pb2'
  # @@protoc_insertion_point(class_scope:CheckOutReply)
  })
_sym_db.RegisterMessage(CheckOutReply)

CheckInReply = _reflection.GeneratedProtocolMessageType('CheckInReply', (_message.Message,), {
  'DESCRIPTOR' : _CHECKINREPLY,
  '__module__' : 'fetch_pb2'
  # @@protoc_insertion_point(class_scope:CheckInReply)
  })
_sym_db.RegisterMessage(CheckInReply)



_FETCH = _descriptor.ServiceDescriptor(
  name='Fetch',
  full_name='Fetch',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=248,
  serialized_end=348,
  methods=[
  _descriptor.MethodDescriptor(
    name='CheckOut',
    full_name='Fetch.CheckOut',
    index=0,
    containing_service=None,
    input_type=_CHECKOUTREQUEST,
    output_type=_CHECKOUTREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CheckIn',
    full_name='Fetch.CheckIn',
    index=1,
    containing_service=None,
    input_type=_CHECKINREQUEST,
    output_type=_CHECKINREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_FETCH)

DESCRIPTOR.services_by_name['Fetch'] = _FETCH

# @@protoc_insertion_point(module_scope)

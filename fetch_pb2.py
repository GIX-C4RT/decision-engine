# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fetch.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
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
  serialized_pb=_b('\n\x0b\x66\x65tch.proto\"V\n\x15\x46\x65tch_CheckOutRequest\x12\x0e\n\x06kit_ID\x18\x01 \x01(\x05\x12\x14\n\x0ckit_location\x18\x02 \x01(\x05\x12\x17\n\x0ftarget_location\x18\x03 \x01(\x05\"U\n\x14\x46\x65tch_CheckInRequest\x12\x0e\n\x06kit_ID\x18\x01 \x01(\x05\x12\x14\n\x0ckit_location\x18\x02 \x01(\x05\x12\x17\n\x0ftarget_location\x18\x03 \x01(\x05\"(\n\x13\x46\x65tch_CheckOutReply\x12\x11\n\tdelivered\x18\x01 \x01(\x08\"&\n\x12\x46\x65tch_CheckInReply\x12\x10\n\x08returned\x18\x01 \x01(\x08\x32\x88\x01\n\x05\x46\x65tch\x12@\n\x0e\x46\x65tch_CheckOut\x12\x16.Fetch_CheckOutRequest\x1a\x14.Fetch_CheckOutReply\"\x00\x12=\n\rFetch_CheckIn\x12\x15.Fetch_CheckInRequest\x1a\x13.Fetch_CheckInReply\"\x00\x62\x06proto3')
)




_FETCH_CHECKOUTREQUEST = _descriptor.Descriptor(
  name='Fetch_CheckOutRequest',
  full_name='Fetch_CheckOutRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='kit_ID', full_name='Fetch_CheckOutRequest.kit_ID', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kit_location', full_name='Fetch_CheckOutRequest.kit_location', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_location', full_name='Fetch_CheckOutRequest.target_location', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=15,
  serialized_end=101,
)


_FETCH_CHECKINREQUEST = _descriptor.Descriptor(
  name='Fetch_CheckInRequest',
  full_name='Fetch_CheckInRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='kit_ID', full_name='Fetch_CheckInRequest.kit_ID', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kit_location', full_name='Fetch_CheckInRequest.kit_location', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_location', full_name='Fetch_CheckInRequest.target_location', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=103,
  serialized_end=188,
)


_FETCH_CHECKOUTREPLY = _descriptor.Descriptor(
  name='Fetch_CheckOutReply',
  full_name='Fetch_CheckOutReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='delivered', full_name='Fetch_CheckOutReply.delivered', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=190,
  serialized_end=230,
)


_FETCH_CHECKINREPLY = _descriptor.Descriptor(
  name='Fetch_CheckInReply',
  full_name='Fetch_CheckInReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='returned', full_name='Fetch_CheckInReply.returned', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=232,
  serialized_end=270,
)

DESCRIPTOR.message_types_by_name['Fetch_CheckOutRequest'] = _FETCH_CHECKOUTREQUEST
DESCRIPTOR.message_types_by_name['Fetch_CheckInRequest'] = _FETCH_CHECKINREQUEST
DESCRIPTOR.message_types_by_name['Fetch_CheckOutReply'] = _FETCH_CHECKOUTREPLY
DESCRIPTOR.message_types_by_name['Fetch_CheckInReply'] = _FETCH_CHECKINREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Fetch_CheckOutRequest = _reflection.GeneratedProtocolMessageType('Fetch_CheckOutRequest', (_message.Message,), dict(
  DESCRIPTOR = _FETCH_CHECKOUTREQUEST,
  __module__ = 'fetch_pb2'
  # @@protoc_insertion_point(class_scope:Fetch_CheckOutRequest)
  ))
_sym_db.RegisterMessage(Fetch_CheckOutRequest)

Fetch_CheckInRequest = _reflection.GeneratedProtocolMessageType('Fetch_CheckInRequest', (_message.Message,), dict(
  DESCRIPTOR = _FETCH_CHECKINREQUEST,
  __module__ = 'fetch_pb2'
  # @@protoc_insertion_point(class_scope:Fetch_CheckInRequest)
  ))
_sym_db.RegisterMessage(Fetch_CheckInRequest)

Fetch_CheckOutReply = _reflection.GeneratedProtocolMessageType('Fetch_CheckOutReply', (_message.Message,), dict(
  DESCRIPTOR = _FETCH_CHECKOUTREPLY,
  __module__ = 'fetch_pb2'
  # @@protoc_insertion_point(class_scope:Fetch_CheckOutReply)
  ))
_sym_db.RegisterMessage(Fetch_CheckOutReply)

Fetch_CheckInReply = _reflection.GeneratedProtocolMessageType('Fetch_CheckInReply', (_message.Message,), dict(
  DESCRIPTOR = _FETCH_CHECKINREPLY,
  __module__ = 'fetch_pb2'
  # @@protoc_insertion_point(class_scope:Fetch_CheckInReply)
  ))
_sym_db.RegisterMessage(Fetch_CheckInReply)



_FETCH = _descriptor.ServiceDescriptor(
  name='Fetch',
  full_name='Fetch',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=273,
  serialized_end=409,
  methods=[
  _descriptor.MethodDescriptor(
    name='Fetch_CheckOut',
    full_name='Fetch.Fetch_CheckOut',
    index=0,
    containing_service=None,
    input_type=_FETCH_CHECKOUTREQUEST,
    output_type=_FETCH_CHECKOUTREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Fetch_CheckIn',
    full_name='Fetch.Fetch_CheckIn',
    index=1,
    containing_service=None,
    input_type=_FETCH_CHECKINREQUEST,
    output_type=_FETCH_CHECKINREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_FETCH)

DESCRIPTOR.services_by_name['Fetch'] = _FETCH

# @@protoc_insertion_point(module_scope)

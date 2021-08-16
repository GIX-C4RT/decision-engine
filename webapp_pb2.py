# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: webapp.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='webapp.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0cwebapp.proto\":\n\x16WebApp_CheckOutRequest\x12\x0f\n\x07user_ID\x18\x01 \x01(\x05\x12\x0f\n\x07item_ID\x18\x02 \x01(\x05\"9\n\x15WebApp_CheckInRequest\x12\x0f\n\x07user_ID\x18\x01 \x01(\x05\x12\x0f\n\x07item_ID\x18\x02 \x01(\x05\"#\n\x14WebApp_CheckOutReply\x12\x0b\n\x03\x61\x63k\x18\x01 \x01(\x08\"\"\n\x13WebApp_CheckInReply\x12\x0b\n\x03\x61\x63k\x18\x01 \x01(\x08\x32\x8f\x01\n\x06WebApp\x12\x43\n\x0fWebApp_CheckOut\x12\x17.WebApp_CheckOutRequest\x1a\x15.WebApp_CheckOutReply\"\x00\x12@\n\x0eWebApp_CheckIn\x12\x16.WebApp_CheckInRequest\x1a\x14.WebApp_CheckInReply\"\x00\x62\x06proto3')
)




_WEBAPP_CHECKOUTREQUEST = _descriptor.Descriptor(
  name='WebApp_CheckOutRequest',
  full_name='WebApp_CheckOutRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_ID', full_name='WebApp_CheckOutRequest.user_ID', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item_ID', full_name='WebApp_CheckOutRequest.item_ID', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=16,
  serialized_end=74,
)


_WEBAPP_CHECKINREQUEST = _descriptor.Descriptor(
  name='WebApp_CheckInRequest',
  full_name='WebApp_CheckInRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_ID', full_name='WebApp_CheckInRequest.user_ID', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item_ID', full_name='WebApp_CheckInRequest.item_ID', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=76,
  serialized_end=133,
)


_WEBAPP_CHECKOUTREPLY = _descriptor.Descriptor(
  name='WebApp_CheckOutReply',
  full_name='WebApp_CheckOutReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ack', full_name='WebApp_CheckOutReply.ack', index=0,
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
  serialized_start=135,
  serialized_end=170,
)


_WEBAPP_CHECKINREPLY = _descriptor.Descriptor(
  name='WebApp_CheckInReply',
  full_name='WebApp_CheckInReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ack', full_name='WebApp_CheckInReply.ack', index=0,
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
  serialized_start=172,
  serialized_end=206,
)

DESCRIPTOR.message_types_by_name['WebApp_CheckOutRequest'] = _WEBAPP_CHECKOUTREQUEST
DESCRIPTOR.message_types_by_name['WebApp_CheckInRequest'] = _WEBAPP_CHECKINREQUEST
DESCRIPTOR.message_types_by_name['WebApp_CheckOutReply'] = _WEBAPP_CHECKOUTREPLY
DESCRIPTOR.message_types_by_name['WebApp_CheckInReply'] = _WEBAPP_CHECKINREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WebApp_CheckOutRequest = _reflection.GeneratedProtocolMessageType('WebApp_CheckOutRequest', (_message.Message,), dict(
  DESCRIPTOR = _WEBAPP_CHECKOUTREQUEST,
  __module__ = 'webapp_pb2'
  # @@protoc_insertion_point(class_scope:WebApp_CheckOutRequest)
  ))
_sym_db.RegisterMessage(WebApp_CheckOutRequest)

WebApp_CheckInRequest = _reflection.GeneratedProtocolMessageType('WebApp_CheckInRequest', (_message.Message,), dict(
  DESCRIPTOR = _WEBAPP_CHECKINREQUEST,
  __module__ = 'webapp_pb2'
  # @@protoc_insertion_point(class_scope:WebApp_CheckInRequest)
  ))
_sym_db.RegisterMessage(WebApp_CheckInRequest)

WebApp_CheckOutReply = _reflection.GeneratedProtocolMessageType('WebApp_CheckOutReply', (_message.Message,), dict(
  DESCRIPTOR = _WEBAPP_CHECKOUTREPLY,
  __module__ = 'webapp_pb2'
  # @@protoc_insertion_point(class_scope:WebApp_CheckOutReply)
  ))
_sym_db.RegisterMessage(WebApp_CheckOutReply)

WebApp_CheckInReply = _reflection.GeneratedProtocolMessageType('WebApp_CheckInReply', (_message.Message,), dict(
  DESCRIPTOR = _WEBAPP_CHECKINREPLY,
  __module__ = 'webapp_pb2'
  # @@protoc_insertion_point(class_scope:WebApp_CheckInReply)
  ))
_sym_db.RegisterMessage(WebApp_CheckInReply)



_WEBAPP = _descriptor.ServiceDescriptor(
  name='WebApp',
  full_name='WebApp',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=209,
  serialized_end=352,
  methods=[
  _descriptor.MethodDescriptor(
    name='WebApp_CheckOut',
    full_name='WebApp.WebApp_CheckOut',
    index=0,
    containing_service=None,
    input_type=_WEBAPP_CHECKOUTREQUEST,
    output_type=_WEBAPP_CHECKOUTREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='WebApp_CheckIn',
    full_name='WebApp.WebApp_CheckIn',
    index=1,
    containing_service=None,
    input_type=_WEBAPP_CHECKINREQUEST,
    output_type=_WEBAPP_CHECKINREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_WEBAPP)

DESCRIPTOR.services_by_name['WebApp'] = _WEBAPP

# @@protoc_insertion_point(module_scope)

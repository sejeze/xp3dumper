# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='xp3proto.proto',
  package='xp3',
  serialized_pb='\n\x0exp3proto.proto\x12\x03xp3\"\x96\x02\n\x07Request\x12&\n\x04type\x18\x01 \x02(\x0e\x32\x18.xp3.Request.RequestType\x12\x0f\n\x07\x65xpAddr\x18\x02 \x01(\x05\x12\x15\n\rfileToExtract\x18\x03 \x03(\t\x12\x13\n\x0b\x65xtractPath\x18\x04 \x01(\t\x12\x15\n\rpngPluginPath\x18\x05 \x01(\t\"\x8e\x01\n\x0bRequestType\x12\x08\n\x04\x45XIT\x10\x00\x12\x13\n\x0fGET_EXPORT_ADDR\x10\x01\x12\x13\n\x0fSET_EXPORT_ADDR\x10\x02\x12\x13\n\x0fINIT_PNG_PLUGIN\x10\x03\x12\x10\n\x0c\x45XTRACT_FILE\x10\x04\x12\x11\n\rALLOC_CONSOLE\x10\x05\x12\x11\n\rPNG_DUMMY_CUT\x10\x06\"@\n\x08Response\x12\x0e\n\x06retVal\x18\x01 \x02(\x05\x12\x0f\n\x07\x65xpAddr\x18\x02 \x01(\x05\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\tB\x02H\x03')



_REQUEST_REQUESTTYPE = descriptor.EnumDescriptor(
  name='RequestType',
  full_name='xp3.Request.RequestType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='EXIT', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='GET_EXPORT_ADDR', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='SET_EXPORT_ADDR', index=2, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='INIT_PNG_PLUGIN', index=3, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='EXTRACT_FILE', index=4, number=4,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ALLOC_CONSOLE', index=5, number=5,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='PNG_DUMMY_CUT', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=160,
  serialized_end=302,
)


_REQUEST = descriptor.Descriptor(
  name='Request',
  full_name='xp3.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='type', full_name='xp3.Request.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='expAddr', full_name='xp3.Request.expAddr', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='fileToExtract', full_name='xp3.Request.fileToExtract', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='extractPath', full_name='xp3.Request.extractPath', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='pngPluginPath', full_name='xp3.Request.pngPluginPath', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REQUEST_REQUESTTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=24,
  serialized_end=302,
)


_RESPONSE = descriptor.Descriptor(
  name='Response',
  full_name='xp3.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='retVal', full_name='xp3.Response.retVal', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='expAddr', full_name='xp3.Response.expAddr', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='description', full_name='xp3.Response.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=304,
  serialized_end=368,
)

_REQUEST.fields_by_name['type'].enum_type = _REQUEST_REQUESTTYPE
_REQUEST_REQUESTTYPE.containing_type = _REQUEST;
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

class Request(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REQUEST
  
  # @@protoc_insertion_point(class_scope:xp3.Request)

class Response(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RESPONSE
  
  # @@protoc_insertion_point(class_scope:xp3.Response)

# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: loopgrpc/compiled/annotations.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from loopgrpc.compiled import http_pb2 as loopgrpc_dot_compiled_dot_http__pb2
from loopgrpc.compiled import descriptor_pb2 as loopgrpc_dot_compiled_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='loopgrpc/compiled/annotations.proto',
  package='google.api',
  syntax='proto3',
  serialized_options=b'\n\016com.google.apiB\020AnnotationsProtoP\001ZAgoogle.golang.org/genproto/googleapis/api/annotations;annotations\242\002\004GAPI',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n#loopgrpc/compiled/annotations.proto\x12\ngoogle.api\x1a\x1cloopgrpc/compiled/http.proto\x1a\"loopgrpc/compiled/descriptor.proto:E\n\x04http\x12\x1e.google.protobuf.MethodOptions\x18\xb0\xca\xbc\" \x01(\x0b\x32\x14.google.api.HttpRuleBn\n\x0e\x63om.google.apiB\x10\x41nnotationsProtoP\x01ZAgoogle.golang.org/genproto/googleapis/api/annotations;annotations\xa2\x02\x04GAPIb\x06proto3'
  ,
  dependencies=[loopgrpc_dot_compiled_dot_http__pb2.DESCRIPTOR,loopgrpc_dot_compiled_dot_descriptor__pb2.DESCRIPTOR,])


HTTP_FIELD_NUMBER = 72295728
http = _descriptor.FieldDescriptor(
  name='http', full_name='google.api.http', index=0,
  number=72295728, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)

DESCRIPTOR.extensions_by_name['http'] = http
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

http.message_type = loopgrpc_dot_compiled_dot_http__pb2._HTTPRULE
loopgrpc_dot_compiled_dot_descriptor__pb2.MethodOptions.RegisterExtension(http)

DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
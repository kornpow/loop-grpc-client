# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: loopgrpc/compiled/debug.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dloopgrpc/compiled/debug.proto\x12\x07looprpc\"\x16\n\x14\x46orceAutoLoopRequest\"\x17\n\x15\x46orceAutoLoopResponse2W\n\x05\x44\x65\x62ug\x12N\n\rForceAutoLoop\x12\x1d.looprpc.ForceAutoLoopRequest\x1a\x1e.looprpc.ForceAutoLoopResponseB\'Z%github.com/lightninglabs/loop/looprpcb\x06proto3')



_FORCEAUTOLOOPREQUEST = DESCRIPTOR.message_types_by_name['ForceAutoLoopRequest']
_FORCEAUTOLOOPRESPONSE = DESCRIPTOR.message_types_by_name['ForceAutoLoopResponse']
ForceAutoLoopRequest = _reflection.GeneratedProtocolMessageType('ForceAutoLoopRequest', (_message.Message,), {
  'DESCRIPTOR' : _FORCEAUTOLOOPREQUEST,
  '__module__' : 'loopgrpc.compiled.debug_pb2'
  # @@protoc_insertion_point(class_scope:looprpc.ForceAutoLoopRequest)
  })
_sym_db.RegisterMessage(ForceAutoLoopRequest)

ForceAutoLoopResponse = _reflection.GeneratedProtocolMessageType('ForceAutoLoopResponse', (_message.Message,), {
  'DESCRIPTOR' : _FORCEAUTOLOOPRESPONSE,
  '__module__' : 'loopgrpc.compiled.debug_pb2'
  # @@protoc_insertion_point(class_scope:looprpc.ForceAutoLoopResponse)
  })
_sym_db.RegisterMessage(ForceAutoLoopResponse)

_DEBUG = DESCRIPTOR.services_by_name['Debug']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z%github.com/lightninglabs/loop/looprpc'
  _FORCEAUTOLOOPREQUEST._serialized_start=42
  _FORCEAUTOLOOPREQUEST._serialized_end=64
  _FORCEAUTOLOOPRESPONSE._serialized_start=66
  _FORCEAUTOLOOPRESPONSE._serialized_end=89
  _DEBUG._serialized_start=91
  _DEBUG._serialized_end=178
# @@protoc_insertion_point(module_scope)

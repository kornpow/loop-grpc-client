# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: loopgrpc/compiled/server.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from loopgrpc.compiled import common_pb2 as loopgrpc_dot_compiled_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eloopgrpc/compiled/server.proto\x12\x07looprpc\x1a\x1eloopgrpc/compiled/common.proto\"\xc7\x01\n\x14ServerLoopOutRequest\x12\x14\n\x0creceiver_key\x18\x01 \x01(\x0c\x12\x11\n\tswap_hash\x18\x02 \x01(\x0c\x12\x0b\n\x03\x61mt\x18\x03 \x01(\x04\x12!\n\x19swap_publication_deadline\x18\x04 \x01(\x03\x12\x32\n\x10protocol_version\x18\x05 \x01(\x0e\x32\x18.looprpc.ProtocolVersion\x12\x0e\n\x06\x65xpiry\x18\x06 \x01(\x05\x12\x12\n\nuser_agent\x18\x07 \x01(\t\"\x85\x01\n\x15ServerLoopOutResponse\x12\x14\n\x0cswap_invoice\x18\x01 \x01(\t\x12\x16\n\x0eprepay_invoice\x18\x02 \x01(\t\x12\x12\n\nsender_key\x18\x03 \x01(\x0c\x12\x12\n\x06\x65xpiry\x18\x04 \x01(\x05\x42\x02\x18\x01\x12\x16\n\x0eserver_message\x18\x05 \x01(\t\"\x8f\x01\n\x19ServerLoopOutQuoteRequest\x12\x0b\n\x03\x61mt\x18\x01 \x01(\x04\x12!\n\x19swap_publication_deadline\x18\x02 \x01(\x03\x12\x32\n\x10protocol_version\x18\x03 \x01(\x0e\x32\x18.looprpc.ProtocolVersion\x12\x0e\n\x06\x65xpiry\x18\x04 \x01(\x05\"\xc2\x01\n\x12ServerLoopOutQuote\x12\x19\n\x11swap_payment_dest\x18\x01 \x01(\t\x12\x10\n\x08swap_fee\x18\x02 \x01(\x03\x12\x19\n\rswap_fee_rate\x18\x03 \x01(\x03\x42\x02\x18\x01\x12\x12\n\nprepay_amt\x18\x04 \x01(\x04\x12\x1b\n\x0fmin_swap_amount\x18\x05 \x01(\x04\x42\x02\x18\x01\x12\x1b\n\x0fmax_swap_amount\x18\x06 \x01(\x04\x42\x02\x18\x01\x12\x16\n\ncltv_delta\x18\x07 \x01(\x05\x42\x02\x18\x01\"O\n\x19ServerLoopOutTermsRequest\x12\x32\n\x10protocol_version\x18\x01 \x01(\x0e\x32\x18.looprpc.ProtocolVersion\"v\n\x12ServerLoopOutTerms\x12\x17\n\x0fmin_swap_amount\x18\x01 \x01(\x04\x12\x17\n\x0fmax_swap_amount\x18\x02 \x01(\x04\x12\x16\n\x0emin_cltv_delta\x18\x03 \x01(\x05\x12\x16\n\x0emax_cltv_delta\x18\x04 \x01(\x05\"\xd0\x01\n\x13ServerLoopInRequest\x12\x12\n\nsender_key\x18\x01 \x01(\x0c\x12\x11\n\tswap_hash\x18\x02 \x01(\x0c\x12\x0b\n\x03\x61mt\x18\x03 \x01(\x04\x12\x14\n\x0cswap_invoice\x18\x04 \x01(\t\x12\x10\n\x08last_hop\x18\x05 \x01(\x0c\x12\x32\n\x10protocol_version\x18\x06 \x01(\x0e\x32\x18.looprpc.ProtocolVersion\x12\x15\n\rprobe_invoice\x18\x07 \x01(\t\x12\x12\n\nuser_agent\x18\x08 \x01(\t\"T\n\x14ServerLoopInResponse\x12\x14\n\x0creceiver_key\x18\x01 \x01(\x0c\x12\x0e\n\x06\x65xpiry\x18\x02 \x01(\x05\x12\x16\n\x0eserver_message\x18\x03 \x01(\t\"\xa6\x01\n\x18ServerLoopInQuoteRequest\x12\x0b\n\x03\x61mt\x18\x01 \x01(\x04\x12\x0e\n\x06pubkey\x18\x03 \x01(\x0c\x12\x10\n\x08last_hop\x18\x04 \x01(\x0c\x12\'\n\x0broute_hints\x18\x05 \x03(\x0b\x32\x12.looprpc.RouteHint\x12\x32\n\x10protocol_version\x18\x02 \x01(\x0e\x32\x18.looprpc.ProtocolVersion\"\x96\x01\n\x19ServerLoopInQuoteResponse\x12\x10\n\x08swap_fee\x18\x01 \x01(\x03\x12\x19\n\rswap_fee_rate\x18\x02 \x01(\x03\x42\x02\x18\x01\x12\x1b\n\x0fmin_swap_amount\x18\x04 \x01(\x04\x42\x02\x18\x01\x12\x1b\n\x0fmax_swap_amount\x18\x05 \x01(\x04\x42\x02\x18\x01\x12\x12\n\ncltv_delta\x18\x06 \x01(\x05\"N\n\x18ServerLoopInTermsRequest\x12\x32\n\x10protocol_version\x18\x01 \x01(\x0e\x32\x18.looprpc.ProtocolVersion\"E\n\x11ServerLoopInTerms\x12\x17\n\x0fmin_swap_amount\x18\x01 \x01(\x04\x12\x17\n\x0fmax_swap_amount\x18\x02 \x01(\x04\"h\n ServerLoopOutPushPreimageRequest\x12\x32\n\x10protocol_version\x18\x01 \x01(\x0e\x32\x18.looprpc.ProtocolVersion\x12\x10\n\x08preimage\x18\x02 \x01(\x0c\"#\n!ServerLoopOutPushPreimageResponse\"`\n\x17SubscribeUpdatesRequest\x12\x32\n\x10protocol_version\x18\x01 \x01(\x0e\x32\x18.looprpc.ProtocolVersion\x12\x11\n\tswap_hash\x18\x02 \x01(\x0c\"`\n\x1fSubscribeLoopOutUpdatesResponse\x12\x14\n\x0ctimestamp_ns\x18\x01 \x01(\x03\x12\'\n\x05state\x18\x02 \x01(\x0e\x32\x18.looprpc.ServerSwapState\"_\n\x1eSubscribeLoopInUpdatesResponse\x12\x14\n\x0ctimestamp_ns\x18\x01 \x01(\x03\x12\'\n\x05state\x18\x02 \x01(\x0e\x32\x18.looprpc.ServerSwapState\"\x94\x01\n\x0bRouteCancel\x12-\n\nroute_type\x18\x01 \x01(\x0e\x32\x19.looprpc.RoutePaymentType\x12&\n\x08\x61ttempts\x18\x02 \x03(\x0b\x32\x14.looprpc.HtlcAttempt\x12.\n\x07\x66\x61ilure\x18\x03 \x01(\x0e\x32\x1d.looprpc.PaymentFailureReason\"%\n\x0bHtlcAttempt\x12\x16\n\x0eremaining_hops\x18\x01 \x01(\r\"\xb7\x01\n\x18\x43\x61ncelLoopOutSwapRequest\x12\x32\n\x10protocol_version\x18\x01 \x01(\x0e\x32\x18.looprpc.ProtocolVersion\x12\x11\n\tswap_hash\x18\x02 \x01(\x0c\x12\x17\n\x0fpayment_address\x18\x03 \x01(\x0c\x12,\n\x0croute_cancel\x18\x05 \x01(\x0b\x32\x14.looprpc.RouteCancelH\x00\x42\r\n\x0b\x63\x61ncel_info\"\x1b\n\x19\x43\x61ncelLoopOutSwapResponse\"\xa0\x01\n\x12ServerProbeRequest\x12\x32\n\x10protocol_version\x18\x01 \x01(\x0e\x32\x18.looprpc.ProtocolVersion\x12\x0b\n\x03\x61mt\x18\x02 \x01(\x04\x12\x0e\n\x06target\x18\x03 \x01(\x0c\x12\x10\n\x08last_hop\x18\x04 \x01(\x0c\x12\'\n\x0broute_hints\x18\x05 \x03(\x0b\x32\x12.looprpc.RouteHint\"\x15\n\x13ServerProbeResponse\"{\n\x19RecommendRoutingPluginReq\x12\x32\n\x10protocol_version\x18\x01 \x01(\x0e\x32\x18.looprpc.ProtocolVersion\x12\x11\n\tswap_hash\x18\x02 \x01(\x0c\x12\x17\n\x0fpayment_address\x18\x03 \x01(\x0c\"C\n\x19RecommendRoutingPluginRes\x12&\n\x06plugin\x18\x01 \x01(\x0e\x32\x16.looprpc.RoutingPlugin\"\xd7\x01\n\x16ReportRoutingResultReq\x12\x32\n\x10protocol_version\x18\x01 \x01(\x0e\x32\x18.looprpc.ProtocolVersion\x12\x11\n\tswap_hash\x18\x02 \x01(\x0c\x12\x17\n\x0fpayment_address\x18\x03 \x01(\x0c\x12&\n\x06plugin\x18\x04 \x01(\x0e\x32\x16.looprpc.RoutingPlugin\x12\x0f\n\x07success\x18\x05 \x01(\x08\x12\x10\n\x08\x61ttempts\x18\x06 \x01(\x05\x12\x12\n\ntotal_time\x18\x07 \x01(\x03\"\x18\n\x16ReportRoutingResultRes*\xd6\x01\n\x0fProtocolVersion\x12\n\n\x06LEGACY\x10\x00\x12\x12\n\x0eMULTI_LOOP_OUT\x10\x01\x12\x19\n\x15NATIVE_SEGWIT_LOOP_IN\x10\x02\x12\x1a\n\x16PREIMAGE_PUSH_LOOP_OUT\x10\x03\x12\x18\n\x14USER_EXPIRY_LOOP_OUT\x10\x04\x12\x0b\n\x07HTLC_V2\x10\x05\x12\x11\n\rMULTI_LOOP_IN\x10\x06\x12\x13\n\x0fLOOP_OUT_CANCEL\x10\x07\x12\t\n\x05PROBE\x10\x08\x12\x12\n\x0eROUTING_PLUGIN\x10\t*\x9e\x04\n\x0fServerSwapState\x12\x14\n\x10SERVER_INITIATED\x10\x00\x12\x19\n\x15SERVER_HTLC_PUBLISHED\x10\x01\x12\x12\n\x0eSERVER_SUCCESS\x10\x02\x12\x19\n\x15SERVER_FAILED_UNKNOWN\x10\x03\x12\x19\n\x15SERVER_FAILED_NO_HTLC\x10\x04\x12%\n!SERVER_FAILED_INVALID_HTLC_AMOUNT\x10\x05\x12#\n\x1fSERVER_FAILED_OFF_CHAIN_TIMEOUT\x10\x06\x12\x19\n\x15SERVER_FAILED_TIMEOUT\x10\x07\x12\x1f\n\x1bSERVER_FAILED_SWAP_DEADLINE\x10\x08\x12\"\n\x1eSERVER_FAILED_HTLC_PUBLICATION\x10\t\x12\x1c\n\x18SERVER_TIMEOUT_PUBLISHED\x10\n\x12\x1d\n\x19SERVER_UNEXPECTED_FAILURE\x10\x0b\x12\x19\n\x15SERVER_HTLC_CONFIRMED\x10\x0c\x12\x1f\n\x1bSERVER_CLIENT_PREPAY_CANCEL\x10\r\x12 \n\x1cSERVER_CLIENT_INVOICE_CANCEL\x10\x0e\x12\'\n#SERVER_FAILED_MULTIPLE_SWAP_SCRIPTS\x10\x0f\x12 \n\x1cSERVER_FAILED_INITIALIZATION\x10\x10*J\n\x10RoutePaymentType\x12\x11\n\rROUTE_UNKNOWN\x10\x00\x12\x10\n\x0cPREPAY_ROUTE\x10\x01\x12\x11\n\rINVOICE_ROUTE\x10\x02*\xf1\x01\n\x14PaymentFailureReason\x12\x1b\n\x17LND_FAILURE_REASON_NONE\x10\x00\x12\x1e\n\x1aLND_FAILURE_REASON_TIMEOUT\x10\x01\x12\x1f\n\x1bLND_FAILURE_REASON_NO_ROUTE\x10\x02\x12\x1c\n\x18LND_FAILURE_REASON_ERROR\x10\x03\x12\x30\n,LND_FAILURE_REASON_INCORRECT_PAYMENT_DETAILS\x10\x04\x12+\n\'LND_FAILURE_REASON_INSUFFICIENT_BALANCE\x10\x05*\'\n\rRoutingPlugin\x12\x08\n\x04NONE\x10\x00\x12\x0c\n\x08LOW_HIGH\x10\x01\x32\x8a\t\n\nSwapServer\x12O\n\x0cLoopOutTerms\x12\".looprpc.ServerLoopOutTermsRequest\x1a\x1b.looprpc.ServerLoopOutTerms\x12O\n\x0eNewLoopOutSwap\x12\x1d.looprpc.ServerLoopOutRequest\x1a\x1e.looprpc.ServerLoopOutResponse\x12l\n\x13LoopOutPushPreimage\x12).looprpc.ServerLoopOutPushPreimageRequest\x1a*.looprpc.ServerLoopOutPushPreimageResponse\x12O\n\x0cLoopOutQuote\x12\".looprpc.ServerLoopOutQuoteRequest\x1a\x1b.looprpc.ServerLoopOutQuote\x12L\n\x0bLoopInTerms\x12!.looprpc.ServerLoopInTermsRequest\x1a\x1a.looprpc.ServerLoopInTerms\x12L\n\rNewLoopInSwap\x12\x1c.looprpc.ServerLoopInRequest\x1a\x1d.looprpc.ServerLoopInResponse\x12T\n\x0bLoopInQuote\x12!.looprpc.ServerLoopInQuoteRequest\x1a\".looprpc.ServerLoopInQuoteResponse\x12g\n\x17SubscribeLoopOutUpdates\x12 .looprpc.SubscribeUpdatesRequest\x1a(.looprpc.SubscribeLoopOutUpdatesResponse0\x01\x12\x65\n\x16SubscribeLoopInUpdates\x12 .looprpc.SubscribeUpdatesRequest\x1a\'.looprpc.SubscribeLoopInUpdatesResponse0\x01\x12Z\n\x11\x43\x61ncelLoopOutSwap\x12!.looprpc.CancelLoopOutSwapRequest\x1a\".looprpc.CancelLoopOutSwapResponse\x12\x42\n\x05Probe\x12\x1b.looprpc.ServerProbeRequest\x1a\x1c.looprpc.ServerProbeResponse\x12`\n\x16RecommendRoutingPlugin\x12\".looprpc.RecommendRoutingPluginReq\x1a\".looprpc.RecommendRoutingPluginRes\x12W\n\x13ReportRoutingResult\x12\x1f.looprpc.ReportRoutingResultReq\x1a\x1f.looprpc.ReportRoutingResultResB-Z+github.com/lightninglabs/loop/swapserverrpcb\x06proto3')

_PROTOCOLVERSION = DESCRIPTOR.enum_types_by_name['ProtocolVersion']
ProtocolVersion = enum_type_wrapper.EnumTypeWrapper(_PROTOCOLVERSION)
_SERVERSWAPSTATE = DESCRIPTOR.enum_types_by_name['ServerSwapState']
ServerSwapState = enum_type_wrapper.EnumTypeWrapper(_SERVERSWAPSTATE)
_ROUTEPAYMENTTYPE = DESCRIPTOR.enum_types_by_name['RoutePaymentType']
RoutePaymentType = enum_type_wrapper.EnumTypeWrapper(_ROUTEPAYMENTTYPE)
_PAYMENTFAILUREREASON = DESCRIPTOR.enum_types_by_name['PaymentFailureReason']
PaymentFailureReason = enum_type_wrapper.EnumTypeWrapper(_PAYMENTFAILUREREASON)
_ROUTINGPLUGIN = DESCRIPTOR.enum_types_by_name['RoutingPlugin']
RoutingPlugin = enum_type_wrapper.EnumTypeWrapper(_ROUTINGPLUGIN)
LEGACY = 0
MULTI_LOOP_OUT = 1
NATIVE_SEGWIT_LOOP_IN = 2
PREIMAGE_PUSH_LOOP_OUT = 3
USER_EXPIRY_LOOP_OUT = 4
HTLC_V2 = 5
MULTI_LOOP_IN = 6
LOOP_OUT_CANCEL = 7
PROBE = 8
ROUTING_PLUGIN = 9
SERVER_INITIATED = 0
SERVER_HTLC_PUBLISHED = 1
SERVER_SUCCESS = 2
SERVER_FAILED_UNKNOWN = 3
SERVER_FAILED_NO_HTLC = 4
SERVER_FAILED_INVALID_HTLC_AMOUNT = 5
SERVER_FAILED_OFF_CHAIN_TIMEOUT = 6
SERVER_FAILED_TIMEOUT = 7
SERVER_FAILED_SWAP_DEADLINE = 8
SERVER_FAILED_HTLC_PUBLICATION = 9
SERVER_TIMEOUT_PUBLISHED = 10
SERVER_UNEXPECTED_FAILURE = 11
SERVER_HTLC_CONFIRMED = 12
SERVER_CLIENT_PREPAY_CANCEL = 13
SERVER_CLIENT_INVOICE_CANCEL = 14
SERVER_FAILED_MULTIPLE_SWAP_SCRIPTS = 15
SERVER_FAILED_INITIALIZATION = 16
ROUTE_UNKNOWN = 0
PREPAY_ROUTE = 1
INVOICE_ROUTE = 2
LND_FAILURE_REASON_NONE = 0
LND_FAILURE_REASON_TIMEOUT = 1
LND_FAILURE_REASON_NO_ROUTE = 2
LND_FAILURE_REASON_ERROR = 3
LND_FAILURE_REASON_INCORRECT_PAYMENT_DETAILS = 4
LND_FAILURE_REASON_INSUFFICIENT_BALANCE = 5
NONE = 0
LOW_HIGH = 1


_SERVERLOOPOUTREQUEST = DESCRIPTOR.message_types_by_name['ServerLoopOutRequest']
_SERVERLOOPOUTRESPONSE = DESCRIPTOR.message_types_by_name['ServerLoopOutResponse']
_SERVERLOOPOUTQUOTEREQUEST = DESCRIPTOR.message_types_by_name['ServerLoopOutQuoteRequest']
_SERVERLOOPOUTQUOTE = DESCRIPTOR.message_types_by_name['ServerLoopOutQuote']
_SERVERLOOPOUTTERMSREQUEST = DESCRIPTOR.message_types_by_name['ServerLoopOutTermsRequest']
_SERVERLOOPOUTTERMS = DESCRIPTOR.message_types_by_name['ServerLoopOutTerms']
_SERVERLOOPINREQUEST = DESCRIPTOR.message_types_by_name['ServerLoopInRequest']
_SERVERLOOPINRESPONSE = DESCRIPTOR.message_types_by_name['ServerLoopInResponse']
_SERVERLOOPINQUOTEREQUEST = DESCRIPTOR.message_types_by_name['ServerLoopInQuoteRequest']
_SERVERLOOPINQUOTERESPONSE = DESCRIPTOR.message_types_by_name['ServerLoopInQuoteResponse']
_SERVERLOOPINTERMSREQUEST = DESCRIPTOR.message_types_by_name['ServerLoopInTermsRequest']
_SERVERLOOPINTERMS = DESCRIPTOR.message_types_by_name['ServerLoopInTerms']
_SERVERLOOPOUTPUSHPREIMAGEREQUEST = DESCRIPTOR.message_types_by_name['ServerLoopOutPushPreimageRequest']
_SERVERLOOPOUTPUSHPREIMAGERESPONSE = DESCRIPTOR.message_types_by_name['ServerLoopOutPushPreimageResponse']
_SUBSCRIBEUPDATESREQUEST = DESCRIPTOR.message_types_by_name['SubscribeUpdatesRequest']
_SUBSCRIBELOOPOUTUPDATESRESPONSE = DESCRIPTOR.message_types_by_name['SubscribeLoopOutUpdatesResponse']
_SUBSCRIBELOOPINUPDATESRESPONSE = DESCRIPTOR.message_types_by_name['SubscribeLoopInUpdatesResponse']
_ROUTECANCEL = DESCRIPTOR.message_types_by_name['RouteCancel']
_HTLCATTEMPT = DESCRIPTOR.message_types_by_name['HtlcAttempt']
_CANCELLOOPOUTSWAPREQUEST = DESCRIPTOR.message_types_by_name['CancelLoopOutSwapRequest']
_CANCELLOOPOUTSWAPRESPONSE = DESCRIPTOR.message_types_by_name['CancelLoopOutSwapResponse']
_SERVERPROBEREQUEST = DESCRIPTOR.message_types_by_name['ServerProbeRequest']
_SERVERPROBERESPONSE = DESCRIPTOR.message_types_by_name['ServerProbeResponse']
_RECOMMENDROUTINGPLUGINREQ = DESCRIPTOR.message_types_by_name['RecommendRoutingPluginReq']
_RECOMMENDROUTINGPLUGINRES = DESCRIPTOR.message_types_by_name['RecommendRoutingPluginRes']
_REPORTROUTINGRESULTREQ = DESCRIPTOR.message_types_by_name['ReportRoutingResultReq']
_REPORTROUTINGRESULTRES = DESCRIPTOR.message_types_by_name['ReportRoutingResultRes']
ServerLoopOutRequest = _reflection.GeneratedProtocolMessageType('ServerLoopOutRequest', (_message.Message,), {
  'DESCRIPTOR' : _SERVERLOOPOUTREQUEST,
  '__module__' : 'loopgrpc.compiled.server_pb2'
  # @@protoc_insertion_point(class_scope:looprpc.ServerLoopOutRequest)
  })
_sym_db.RegisterMessage(ServerLoopOutRequest)

ServerLoopOutResponse = _reflection.GeneratedProtocolMessageType('ServerLoopOutResponse', (_message.Message,), {
  'DESCRIPTOR' : _SERVERLOOPOUTRESPONSE,
  '__module__' : 'loopgrpc.compiled.server_pb2'
  # @@protoc_insertion_point(class_scope:looprpc.ServerLoopOutResponse)
  })
_sym_db.RegisterMessage(ServerLoopOutResponse)

ServerLoopOutQuoteRequest = _reflection.GeneratedProtocolMessageType('ServerLoopOutQuoteRequest', (_message.Message,), {
  'DESCRIPTOR' : _SERVERLOOPOUTQUOTEREQUEST,
  '__module__' : 'loopgrpc.compiled.server_pb2'
  # @@protoc_insertion_point(class_scope:looprpc.ServerLoopOutQuoteRequest)
  })
_sym_db.RegisterMessage(ServerLoopOutQuoteRequest)

ServerLoopOutQuote = _reflection.GeneratedProtocolMessageType('ServerLoopOutQuote', (_message.Message,), {
  'DESCRIPTOR' : _SERVERLOOPOUTQUOTE,
  '__module__' : 'loopgrpc.compiled.server_pb2'
  # @@protoc_insertion_point(class_scope:looprpc.ServerLoopOutQuote)
  })
_sym_db.RegisterMessage(ServerLoopOutQuote)

ServerLoopOutTermsRequest = _reflection.GeneratedProtocolMessageType('ServerLoopOutTermsRequest', (_message.Message,), {
  'DESCRIPTOR' : _SERVERLOOPOUTTERMSREQUEST,
  '__module__' : 'loopgrpc.compiled.server_pb2'
  # @@protoc_insertion_point(class_scope:looprpc.ServerLoopOutTermsRequest)
  })
_sym_db.RegisterMessage(ServerLoopOutTermsRequest)

ServerLoopOutTerms = _reflection.GeneratedProtocolMessageType('ServerLoopOutTerms', (_message.Message,), {
  'DESCRIPTOR' : _SERVERLOOPOUTTERMS,
  '__module__' : 'loopgrpc.compiled.server_pb2'
  # @@protoc_insertion_point(class_scope:looprpc.ServerLoopOutTerms)
  })
_sym_db.RegisterMessage(ServerLoopOutTerms)

ServerLoopInRequest = _reflection.GeneratedProtocolMessageType('ServerLoopInRequest', (_message.Message,), {
  'DESCRIPTOR' : _SERVERLOOPINREQUEST,
  '__module__' : 'loopgrpc.compiled.server_pb2'
  # @@protoc_insertion_point(class_scope:looprpc.ServerLoopInRequest)
  })
_sym_db.RegisterMessage(ServerLoopInRequest)

ServerLoopInResponse = _reflection.GeneratedProtocolMessageType('ServerLoopInResponse', (_message.Message,), {
  'DESCRIPTOR' : _SERVERLOOPINRESPONSE,
  '__module__' : 'loopgrpc.compiled.server_pb2'
  # @@protoc_insertion_point(class_scope:looprpc.ServerLoopInResponse)
  })
_sym_db.RegisterMessage(ServerLoopInResponse)

ServerLoopInQuoteRequest = _reflection.GeneratedProtocolMessageType('ServerLoopInQuoteRequest', (_message.Message,), {
  'DESCRIPTOR' : _SERVERLOOPINQUOTEREQUEST,
  '__module__' : 'loopgrpc.compiled.server_pb2'
  # @@protoc_insertion_point(class_scope:looprpc.ServerLoopInQuoteRequest)
  })
_sym_db.RegisterMessage(ServerLoopInQuoteRequest)

ServerLoopInQuoteResponse = _reflection.GeneratedProtocolMessageType('ServerLoopInQuoteResponse', (_message.Message,), {
  'DESCRIPTOR' : _SERVERLOOPINQUOTERESPONSE,
  '__module__' : 'loopgrpc.compiled.server_pb2'
  # @@protoc_insertion_point(class_scope:looprpc.ServerLoopInQuoteResponse)
  })
_sym_db.RegisterMessage(ServerLoopInQuoteResponse)

ServerLoopInTermsRequest = _reflection.GeneratedProtocolMessageType('ServerLoopInTermsRequest', (_message.Message,), {
  'DESCRIPTOR' : _SERVERLOOPINTERMSREQUEST,
  '__module__' : 'loopgrpc.compiled.server_pb2'
  # @@protoc_insertion_point(class_scope:looprpc.ServerLoopInTermsRequest)
  })
_sym_db.RegisterMessage(ServerLoopInTermsRequest)

ServerLoopInTerms = _reflection.GeneratedProtocolMessageType('ServerLoopInTerms', (_message.Message,), {
  'DESCRIPTOR' : _SERVERLOOPINTERMS,
  '__module__' : 'loopgrpc.compiled.server_pb2'
  # @@protoc_insertion_point(class_scope:looprpc.ServerLoopInTerms)
  })
_sym_db.RegisterMessage(ServerLoopInTerms)

ServerLoopOutPushPreimageRequest = _reflection.GeneratedProtocolMessageType('ServerLoopOutPushPreimageRequest', (_message.Message,), {
  'DESCRIPTOR' : _SERVERLOOPOUTPUSHPREIMAGEREQUEST,
  '__module__' : 'loopgrpc.compiled.server_pb2'
  # @@protoc_insertion_point(class_scope:looprpc.ServerLoopOutPushPreimageRequest)
  })
_sym_db.RegisterMessage(ServerLoopOutPushPreimageRequest)

ServerLoopOutPushPreimageResponse = _reflection.GeneratedProtocolMessageType('ServerLoopOutPushPreimageResponse', (_message.Message,), {
  'DESCRIPTOR' : _SERVERLOOPOUTPUSHPREIMAGERESPONSE,
  '__module__' : 'loopgrpc.compiled.server_pb2'
  # @@protoc_insertion_point(class_scope:looprpc.ServerLoopOutPushPreimageResponse)
  })
_sym_db.RegisterMessage(ServerLoopOutPushPreimageResponse)

SubscribeUpdatesRequest = _reflection.GeneratedProtocolMessageType('SubscribeUpdatesRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBEUPDATESREQUEST,
  '__module__' : 'loopgrpc.compiled.server_pb2'
  # @@protoc_insertion_point(class_scope:looprpc.SubscribeUpdatesRequest)
  })
_sym_db.RegisterMessage(SubscribeUpdatesRequest)

SubscribeLoopOutUpdatesResponse = _reflection.GeneratedProtocolMessageType('SubscribeLoopOutUpdatesResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBELOOPOUTUPDATESRESPONSE,
  '__module__' : 'loopgrpc.compiled.server_pb2'
  # @@protoc_insertion_point(class_scope:looprpc.SubscribeLoopOutUpdatesResponse)
  })
_sym_db.RegisterMessage(SubscribeLoopOutUpdatesResponse)

SubscribeLoopInUpdatesResponse = _reflection.GeneratedProtocolMessageType('SubscribeLoopInUpdatesResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBELOOPINUPDATESRESPONSE,
  '__module__' : 'loopgrpc.compiled.server_pb2'
  # @@protoc_insertion_point(class_scope:looprpc.SubscribeLoopInUpdatesResponse)
  })
_sym_db.RegisterMessage(SubscribeLoopInUpdatesResponse)

RouteCancel = _reflection.GeneratedProtocolMessageType('RouteCancel', (_message.Message,), {
  'DESCRIPTOR' : _ROUTECANCEL,
  '__module__' : 'loopgrpc.compiled.server_pb2'
  # @@protoc_insertion_point(class_scope:looprpc.RouteCancel)
  })
_sym_db.RegisterMessage(RouteCancel)

HtlcAttempt = _reflection.GeneratedProtocolMessageType('HtlcAttempt', (_message.Message,), {
  'DESCRIPTOR' : _HTLCATTEMPT,
  '__module__' : 'loopgrpc.compiled.server_pb2'
  # @@protoc_insertion_point(class_scope:looprpc.HtlcAttempt)
  })
_sym_db.RegisterMessage(HtlcAttempt)

CancelLoopOutSwapRequest = _reflection.GeneratedProtocolMessageType('CancelLoopOutSwapRequest', (_message.Message,), {
  'DESCRIPTOR' : _CANCELLOOPOUTSWAPREQUEST,
  '__module__' : 'loopgrpc.compiled.server_pb2'
  # @@protoc_insertion_point(class_scope:looprpc.CancelLoopOutSwapRequest)
  })
_sym_db.RegisterMessage(CancelLoopOutSwapRequest)

CancelLoopOutSwapResponse = _reflection.GeneratedProtocolMessageType('CancelLoopOutSwapResponse', (_message.Message,), {
  'DESCRIPTOR' : _CANCELLOOPOUTSWAPRESPONSE,
  '__module__' : 'loopgrpc.compiled.server_pb2'
  # @@protoc_insertion_point(class_scope:looprpc.CancelLoopOutSwapResponse)
  })
_sym_db.RegisterMessage(CancelLoopOutSwapResponse)

ServerProbeRequest = _reflection.GeneratedProtocolMessageType('ServerProbeRequest', (_message.Message,), {
  'DESCRIPTOR' : _SERVERPROBEREQUEST,
  '__module__' : 'loopgrpc.compiled.server_pb2'
  # @@protoc_insertion_point(class_scope:looprpc.ServerProbeRequest)
  })
_sym_db.RegisterMessage(ServerProbeRequest)

ServerProbeResponse = _reflection.GeneratedProtocolMessageType('ServerProbeResponse', (_message.Message,), {
  'DESCRIPTOR' : _SERVERPROBERESPONSE,
  '__module__' : 'loopgrpc.compiled.server_pb2'
  # @@protoc_insertion_point(class_scope:looprpc.ServerProbeResponse)
  })
_sym_db.RegisterMessage(ServerProbeResponse)

RecommendRoutingPluginReq = _reflection.GeneratedProtocolMessageType('RecommendRoutingPluginReq', (_message.Message,), {
  'DESCRIPTOR' : _RECOMMENDROUTINGPLUGINREQ,
  '__module__' : 'loopgrpc.compiled.server_pb2'
  # @@protoc_insertion_point(class_scope:looprpc.RecommendRoutingPluginReq)
  })
_sym_db.RegisterMessage(RecommendRoutingPluginReq)

RecommendRoutingPluginRes = _reflection.GeneratedProtocolMessageType('RecommendRoutingPluginRes', (_message.Message,), {
  'DESCRIPTOR' : _RECOMMENDROUTINGPLUGINRES,
  '__module__' : 'loopgrpc.compiled.server_pb2'
  # @@protoc_insertion_point(class_scope:looprpc.RecommendRoutingPluginRes)
  })
_sym_db.RegisterMessage(RecommendRoutingPluginRes)

ReportRoutingResultReq = _reflection.GeneratedProtocolMessageType('ReportRoutingResultReq', (_message.Message,), {
  'DESCRIPTOR' : _REPORTROUTINGRESULTREQ,
  '__module__' : 'loopgrpc.compiled.server_pb2'
  # @@protoc_insertion_point(class_scope:looprpc.ReportRoutingResultReq)
  })
_sym_db.RegisterMessage(ReportRoutingResultReq)

ReportRoutingResultRes = _reflection.GeneratedProtocolMessageType('ReportRoutingResultRes', (_message.Message,), {
  'DESCRIPTOR' : _REPORTROUTINGRESULTRES,
  '__module__' : 'loopgrpc.compiled.server_pb2'
  # @@protoc_insertion_point(class_scope:looprpc.ReportRoutingResultRes)
  })
_sym_db.RegisterMessage(ReportRoutingResultRes)

_SWAPSERVER = DESCRIPTOR.services_by_name['SwapServer']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z+github.com/lightninglabs/loop/swapserverrpc'
  _SERVERLOOPOUTRESPONSE.fields_by_name['expiry']._options = None
  _SERVERLOOPOUTRESPONSE.fields_by_name['expiry']._serialized_options = b'\030\001'
  _SERVERLOOPOUTQUOTE.fields_by_name['swap_fee_rate']._options = None
  _SERVERLOOPOUTQUOTE.fields_by_name['swap_fee_rate']._serialized_options = b'\030\001'
  _SERVERLOOPOUTQUOTE.fields_by_name['min_swap_amount']._options = None
  _SERVERLOOPOUTQUOTE.fields_by_name['min_swap_amount']._serialized_options = b'\030\001'
  _SERVERLOOPOUTQUOTE.fields_by_name['max_swap_amount']._options = None
  _SERVERLOOPOUTQUOTE.fields_by_name['max_swap_amount']._serialized_options = b'\030\001'
  _SERVERLOOPOUTQUOTE.fields_by_name['cltv_delta']._options = None
  _SERVERLOOPOUTQUOTE.fields_by_name['cltv_delta']._serialized_options = b'\030\001'
  _SERVERLOOPINQUOTERESPONSE.fields_by_name['swap_fee_rate']._options = None
  _SERVERLOOPINQUOTERESPONSE.fields_by_name['swap_fee_rate']._serialized_options = b'\030\001'
  _SERVERLOOPINQUOTERESPONSE.fields_by_name['min_swap_amount']._options = None
  _SERVERLOOPINQUOTERESPONSE.fields_by_name['min_swap_amount']._serialized_options = b'\030\001'
  _SERVERLOOPINQUOTERESPONSE.fields_by_name['max_swap_amount']._options = None
  _SERVERLOOPINQUOTERESPONSE.fields_by_name['max_swap_amount']._serialized_options = b'\030\001'
  _PROTOCOLVERSION._serialized_start=3193
  _PROTOCOLVERSION._serialized_end=3407
  _SERVERSWAPSTATE._serialized_start=3410
  _SERVERSWAPSTATE._serialized_end=3952
  _ROUTEPAYMENTTYPE._serialized_start=3954
  _ROUTEPAYMENTTYPE._serialized_end=4028
  _PAYMENTFAILUREREASON._serialized_start=4031
  _PAYMENTFAILUREREASON._serialized_end=4272
  _ROUTINGPLUGIN._serialized_start=4274
  _ROUTINGPLUGIN._serialized_end=4313
  _SERVERLOOPOUTREQUEST._serialized_start=76
  _SERVERLOOPOUTREQUEST._serialized_end=275
  _SERVERLOOPOUTRESPONSE._serialized_start=278
  _SERVERLOOPOUTRESPONSE._serialized_end=411
  _SERVERLOOPOUTQUOTEREQUEST._serialized_start=414
  _SERVERLOOPOUTQUOTEREQUEST._serialized_end=557
  _SERVERLOOPOUTQUOTE._serialized_start=560
  _SERVERLOOPOUTQUOTE._serialized_end=754
  _SERVERLOOPOUTTERMSREQUEST._serialized_start=756
  _SERVERLOOPOUTTERMSREQUEST._serialized_end=835
  _SERVERLOOPOUTTERMS._serialized_start=837
  _SERVERLOOPOUTTERMS._serialized_end=955
  _SERVERLOOPINREQUEST._serialized_start=958
  _SERVERLOOPINREQUEST._serialized_end=1166
  _SERVERLOOPINRESPONSE._serialized_start=1168
  _SERVERLOOPINRESPONSE._serialized_end=1252
  _SERVERLOOPINQUOTEREQUEST._serialized_start=1255
  _SERVERLOOPINQUOTEREQUEST._serialized_end=1421
  _SERVERLOOPINQUOTERESPONSE._serialized_start=1424
  _SERVERLOOPINQUOTERESPONSE._serialized_end=1574
  _SERVERLOOPINTERMSREQUEST._serialized_start=1576
  _SERVERLOOPINTERMSREQUEST._serialized_end=1654
  _SERVERLOOPINTERMS._serialized_start=1656
  _SERVERLOOPINTERMS._serialized_end=1725
  _SERVERLOOPOUTPUSHPREIMAGEREQUEST._serialized_start=1727
  _SERVERLOOPOUTPUSHPREIMAGEREQUEST._serialized_end=1831
  _SERVERLOOPOUTPUSHPREIMAGERESPONSE._serialized_start=1833
  _SERVERLOOPOUTPUSHPREIMAGERESPONSE._serialized_end=1868
  _SUBSCRIBEUPDATESREQUEST._serialized_start=1870
  _SUBSCRIBEUPDATESREQUEST._serialized_end=1966
  _SUBSCRIBELOOPOUTUPDATESRESPONSE._serialized_start=1968
  _SUBSCRIBELOOPOUTUPDATESRESPONSE._serialized_end=2064
  _SUBSCRIBELOOPINUPDATESRESPONSE._serialized_start=2066
  _SUBSCRIBELOOPINUPDATESRESPONSE._serialized_end=2161
  _ROUTECANCEL._serialized_start=2164
  _ROUTECANCEL._serialized_end=2312
  _HTLCATTEMPT._serialized_start=2314
  _HTLCATTEMPT._serialized_end=2351
  _CANCELLOOPOUTSWAPREQUEST._serialized_start=2354
  _CANCELLOOPOUTSWAPREQUEST._serialized_end=2537
  _CANCELLOOPOUTSWAPRESPONSE._serialized_start=2539
  _CANCELLOOPOUTSWAPRESPONSE._serialized_end=2566
  _SERVERPROBEREQUEST._serialized_start=2569
  _SERVERPROBEREQUEST._serialized_end=2729
  _SERVERPROBERESPONSE._serialized_start=2731
  _SERVERPROBERESPONSE._serialized_end=2752
  _RECOMMENDROUTINGPLUGINREQ._serialized_start=2754
  _RECOMMENDROUTINGPLUGINREQ._serialized_end=2877
  _RECOMMENDROUTINGPLUGINRES._serialized_start=2879
  _RECOMMENDROUTINGPLUGINRES._serialized_end=2946
  _REPORTROUTINGRESULTREQ._serialized_start=2949
  _REPORTROUTINGRESULTREQ._serialized_end=3164
  _REPORTROUTINGRESULTRES._serialized_start=3166
  _REPORTROUTINGRESULTRES._serialized_end=3190
  _SWAPSERVER._serialized_start=4316
  _SWAPSERVER._serialized_end=5478
# @@protoc_insertion_point(module_scope)

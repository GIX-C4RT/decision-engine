# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import kinova_pb2 as kinova__pb2


class KinovaStub(object):
    """The Kinova service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CheckOut = channel.unary_unary(
                '/Kinova/CheckOut',
                request_serializer=kinova__pb2.CheckOutRequest.SerializeToString,
                response_deserializer=kinova__pb2.CheckOutReply.FromString,
                )
        self.CheckIn = channel.unary_unary(
                '/Kinova/CheckIn',
                request_serializer=kinova__pb2.CheckInRequest.SerializeToString,
                response_deserializer=kinova__pb2.CheckInReply.FromString,
                )


class KinovaServicer(object):
    """The Kinova service definition.
    """

    def CheckOut(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckIn(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_KinovaServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CheckOut': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckOut,
                    request_deserializer=kinova__pb2.CheckOutRequest.FromString,
                    response_serializer=kinova__pb2.CheckOutReply.SerializeToString,
            ),
            'CheckIn': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckIn,
                    request_deserializer=kinova__pb2.CheckInRequest.FromString,
                    response_serializer=kinova__pb2.CheckInReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Kinova', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Kinova(object):
    """The Kinova service definition.
    """

    @staticmethod
    def CheckOut(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Kinova/CheckOut',
            kinova__pb2.CheckOutRequest.SerializeToString,
            kinova__pb2.CheckOutReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckIn(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Kinova/CheckIn',
            kinova__pb2.CheckInRequest.SerializeToString,
            kinova__pb2.CheckInReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

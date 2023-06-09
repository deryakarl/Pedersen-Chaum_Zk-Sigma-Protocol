# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import zkp_pb2 as zkp__pb2


class ZKPStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Register = channel.unary_unary(
                '/zkp.ZKP/Register',
                request_serializer=zkp__pb2.RegistrationRequest.SerializeToString,
                response_deserializer=zkp__pb2.RegistrationResponse.FromString,
                )
        self.Authenticate = channel.unary_unary(
                '/zkp.ZKP/Authenticate',
                request_serializer=zkp__pb2.AuthenticationRequest.SerializeToString,
                response_deserializer=zkp__pb2.AuthenticationResponse.FromString,
                )


class ZKPServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Register(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Authenticate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ZKPServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Register': grpc.unary_unary_rpc_method_handler(
                    servicer.Register,
                    request_deserializer=zkp__pb2.RegistrationRequest.FromString,
                    response_serializer=zkp__pb2.RegistrationResponse.SerializeToString,
            ),
            'Authenticate': grpc.unary_unary_rpc_method_handler(
                    servicer.Authenticate,
                    request_deserializer=zkp__pb2.AuthenticationRequest.FromString,
                    response_serializer=zkp__pb2.AuthenticationResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'zkp.ZKP', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ZKP(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Register(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/zkp.ZKP/Register',
            zkp__pb2.RegistrationRequest.SerializeToString,
            zkp__pb2.RegistrationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Authenticate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/zkp.ZKP/Authenticate',
            zkp__pb2.AuthenticationRequest.SerializeToString,
            zkp__pb2.AuthenticationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

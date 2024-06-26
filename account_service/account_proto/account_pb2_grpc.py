# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from account_proto import account_pb2 as account__proto_dot_account__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class AccountControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_stream(
                '/account.AccountController/List',
                request_serializer=account__proto_dot_account__pb2.AccountListRequest.SerializeToString,
                response_deserializer=account__proto_dot_account__pb2.Account.FromString,
                )
        self.Create = channel.unary_unary(
                '/account.AccountController/Create',
                request_serializer=account__proto_dot_account__pb2.Account.SerializeToString,
                response_deserializer=account__proto_dot_account__pb2.Account.FromString,
                )
        self.Retrieve = channel.unary_unary(
                '/account.AccountController/Retrieve',
                request_serializer=account__proto_dot_account__pb2.AccountRetrieveRequest.SerializeToString,
                response_deserializer=account__proto_dot_account__pb2.Account.FromString,
                )
        self.RetrieveByCustomer = channel.unary_stream(
                '/account.AccountController/RetrieveByCustomer',
                request_serializer=account__proto_dot_account__pb2.AccountRetrieveByCustomerRequest.SerializeToString,
                response_deserializer=account__proto_dot_account__pb2.Account.FromString,
                )
        self.Update = channel.unary_unary(
                '/account.AccountController/Update',
                request_serializer=account__proto_dot_account__pb2.Account.SerializeToString,
                response_deserializer=account__proto_dot_account__pb2.Account.FromString,
                )
        self.Destroy = channel.unary_unary(
                '/account.AccountController/Destroy',
                request_serializer=account__proto_dot_account__pb2.Account.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.DestroyAll = channel.unary_unary(
                '/account.AccountController/DestroyAll',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class AccountControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Retrieve(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RetrieveByCustomer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Destroy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DestroyAll(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AccountControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_stream_rpc_method_handler(
                    servicer.List,
                    request_deserializer=account__proto_dot_account__pb2.AccountListRequest.FromString,
                    response_serializer=account__proto_dot_account__pb2.Account.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=account__proto_dot_account__pb2.Account.FromString,
                    response_serializer=account__proto_dot_account__pb2.Account.SerializeToString,
            ),
            'Retrieve': grpc.unary_unary_rpc_method_handler(
                    servicer.Retrieve,
                    request_deserializer=account__proto_dot_account__pb2.AccountRetrieveRequest.FromString,
                    response_serializer=account__proto_dot_account__pb2.Account.SerializeToString,
            ),
            'RetrieveByCustomer': grpc.unary_stream_rpc_method_handler(
                    servicer.RetrieveByCustomer,
                    request_deserializer=account__proto_dot_account__pb2.AccountRetrieveByCustomerRequest.FromString,
                    response_serializer=account__proto_dot_account__pb2.Account.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=account__proto_dot_account__pb2.Account.FromString,
                    response_serializer=account__proto_dot_account__pb2.Account.SerializeToString,
            ),
            'Destroy': grpc.unary_unary_rpc_method_handler(
                    servicer.Destroy,
                    request_deserializer=account__proto_dot_account__pb2.Account.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'DestroyAll': grpc.unary_unary_rpc_method_handler(
                    servicer.DestroyAll,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'account.AccountController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AccountController(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/account.AccountController/List',
            account__proto_dot_account__pb2.AccountListRequest.SerializeToString,
            account__proto_dot_account__pb2.Account.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/account.AccountController/Create',
            account__proto_dot_account__pb2.Account.SerializeToString,
            account__proto_dot_account__pb2.Account.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Retrieve(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/account.AccountController/Retrieve',
            account__proto_dot_account__pb2.AccountRetrieveRequest.SerializeToString,
            account__proto_dot_account__pb2.Account.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RetrieveByCustomer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/account.AccountController/RetrieveByCustomer',
            account__proto_dot_account__pb2.AccountRetrieveByCustomerRequest.SerializeToString,
            account__proto_dot_account__pb2.Account.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/account.AccountController/Update',
            account__proto_dot_account__pb2.Account.SerializeToString,
            account__proto_dot_account__pb2.Account.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Destroy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/account.AccountController/Destroy',
            account__proto_dot_account__pb2.Account.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DestroyAll(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/account.AccountController/DestroyAll',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

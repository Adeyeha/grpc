# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from customer_proto import customer_pb2 as customer__proto_dot_customer__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class CustomerControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_stream(
                '/customer.CustomerController/List',
                request_serializer=customer__proto_dot_customer__pb2.CustomerListRequest.SerializeToString,
                response_deserializer=customer__proto_dot_customer__pb2.Customer.FromString,
                )
        self.Create = channel.unary_unary(
                '/customer.CustomerController/Create',
                request_serializer=customer__proto_dot_customer__pb2.Customer.SerializeToString,
                response_deserializer=customer__proto_dot_customer__pb2.Customer.FromString,
                )
        self.Retrieve = channel.unary_unary(
                '/customer.CustomerController/Retrieve',
                request_serializer=customer__proto_dot_customer__pb2.CustomerRetrieveRequest.SerializeToString,
                response_deserializer=customer__proto_dot_customer__pb2.Customer.FromString,
                )
        self.RetrievebyPhone = channel.unary_unary(
                '/customer.CustomerController/RetrievebyPhone',
                request_serializer=customer__proto_dot_customer__pb2.CustomerRetrievebyPhoneRequest.SerializeToString,
                response_deserializer=customer__proto_dot_customer__pb2.Customer.FromString,
                )
        self.Update = channel.unary_unary(
                '/customer.CustomerController/Update',
                request_serializer=customer__proto_dot_customer__pb2.Customer.SerializeToString,
                response_deserializer=customer__proto_dot_customer__pb2.Customer.FromString,
                )
        self.Destroy = channel.unary_unary(
                '/customer.CustomerController/Destroy',
                request_serializer=customer__proto_dot_customer__pb2.Customer.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.DestroyAll = channel.unary_unary(
                '/customer.CustomerController/DestroyAll',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class CustomerControllerServicer(object):
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

    def RetrievebyPhone(self, request, context):
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


def add_CustomerControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_stream_rpc_method_handler(
                    servicer.List,
                    request_deserializer=customer__proto_dot_customer__pb2.CustomerListRequest.FromString,
                    response_serializer=customer__proto_dot_customer__pb2.Customer.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=customer__proto_dot_customer__pb2.Customer.FromString,
                    response_serializer=customer__proto_dot_customer__pb2.Customer.SerializeToString,
            ),
            'Retrieve': grpc.unary_unary_rpc_method_handler(
                    servicer.Retrieve,
                    request_deserializer=customer__proto_dot_customer__pb2.CustomerRetrieveRequest.FromString,
                    response_serializer=customer__proto_dot_customer__pb2.Customer.SerializeToString,
            ),
            'RetrievebyPhone': grpc.unary_unary_rpc_method_handler(
                    servicer.RetrievebyPhone,
                    request_deserializer=customer__proto_dot_customer__pb2.CustomerRetrievebyPhoneRequest.FromString,
                    response_serializer=customer__proto_dot_customer__pb2.Customer.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=customer__proto_dot_customer__pb2.Customer.FromString,
                    response_serializer=customer__proto_dot_customer__pb2.Customer.SerializeToString,
            ),
            'Destroy': grpc.unary_unary_rpc_method_handler(
                    servicer.Destroy,
                    request_deserializer=customer__proto_dot_customer__pb2.Customer.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'DestroyAll': grpc.unary_unary_rpc_method_handler(
                    servicer.DestroyAll,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'customer.CustomerController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CustomerController(object):
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
        return grpc.experimental.unary_stream(request, target, '/customer.CustomerController/List',
            customer__proto_dot_customer__pb2.CustomerListRequest.SerializeToString,
            customer__proto_dot_customer__pb2.Customer.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/customer.CustomerController/Create',
            customer__proto_dot_customer__pb2.Customer.SerializeToString,
            customer__proto_dot_customer__pb2.Customer.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/customer.CustomerController/Retrieve',
            customer__proto_dot_customer__pb2.CustomerRetrieveRequest.SerializeToString,
            customer__proto_dot_customer__pb2.Customer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RetrievebyPhone(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/customer.CustomerController/RetrievebyPhone',
            customer__proto_dot_customer__pb2.CustomerRetrievebyPhoneRequest.SerializeToString,
            customer__proto_dot_customer__pb2.Customer.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/customer.CustomerController/Update',
            customer__proto_dot_customer__pb2.Customer.SerializeToString,
            customer__proto_dot_customer__pb2.Customer.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/customer.CustomerController/Destroy',
            customer__proto_dot_customer__pb2.Customer.SerializeToString,
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
        return grpc.experimental.unary_unary(request, target, '/customer.CustomerController/DestroyAll',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

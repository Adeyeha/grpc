from customer.services import CustomerService
from customer_proto import customer_pb2_grpc


def grpc_handlers(server):
    customer_pb2_grpc.add_CustomerControllerServicer_to_server(CustomerService.as_servicer(), server)
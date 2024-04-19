from transaction.services import TransactionService
from transaction_proto import transaction_pb2_grpc


def grpc_handlers(server):
    transaction_pb2_grpc.add_TransactionControllerServicer_to_server(TransactionService.as_servicer(), server)
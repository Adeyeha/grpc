from account.services import AccountService
from account_proto import account_pb2_grpc


def grpc_handlers(server):
    account_pb2_grpc.add_AccountControllerServicer_to_server(AccountService.as_servicer(), server)
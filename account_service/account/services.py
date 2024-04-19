import grpc
from google.protobuf import empty_pb2
from django_grpc_framework.services import Service
from account.models import Account
from account.proto_serializers import AccountProtoSerializer


class AccountService(Service):
    def List(self, request, context):
        accounts = Account.objects.all()
        serializer = AccountProtoSerializer(accounts, many=True)
        for msg in serializer.message:
            yield msg

    def Create(self, request, context):
        serializer = AccountProtoSerializer(message=request)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.message

    def get_object(self, pk):
        try:
            return Account.objects.get(pk=pk)
        except Account.DoesNotExist:
            self.context.abort(grpc.StatusCode.NOT_FOUND, 'Account:%s not found!' % pk)

    def Retrieve(self, request, context):
        account = self.get_object(request.account_number)
        serializer = AccountProtoSerializer(account)
        return serializer.message

    def RetrieveByCustomer(self, request, context):
        accounts = Account.objects.filter(customer_id=request.customer_id)
        serializer = AccountProtoSerializer(accounts, many=True)
        for msg in serializer.message:
            yield msg    

    def Update(self, request, context):
        account = self.get_object(request.account_number)
        serializer = AccountProtoSerializer(account, message=request)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.message

    def Destroy(self, request, context):
        account = self.get_object(request.account_number)
        account.delete()
        return empty_pb2.Empty()
    
    def DestroyAll(self, request, context):
        Account.objects.all().delete()
        return empty_pb2.Empty()
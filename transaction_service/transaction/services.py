import grpc
from google.protobuf import empty_pb2
from django_grpc_framework.services import Service
from transaction.models import Transaction
from transaction.proto_serializers import TransactionProtoSerializer


class TransactionService(Service):
    def List(self, request, context):
        transactions = Transaction.objects.all()
        serializer = TransactionProtoSerializer(transactions, many=True)
        for msg in serializer.message:
            yield msg

    def Create(self, request, context):
        serializer = TransactionProtoSerializer(message=request)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.message

    def get_object(self, pk):
        try:
            return Transaction.objects.get(pk=pk)
        except Transaction.DoesNotExist:
            self.context.abort(grpc.StatusCode.NOT_FOUND, 'Transaction:%s not found!' % pk)

    def Retrieve(self, request, context):
        transaction = self.get_object(request.transaction_id)
        serializer = TransactionProtoSerializer(transaction)
        return serializer.message

    def RetrieveByAccount(self, request, context):
        accounts = Transaction.objects.filter(account=request.account)
        serializer = TransactionProtoSerializer(accounts, many=True)
        for msg in serializer.message:
            yield msg   

    def Update(self, request, context):
        transaction = self.get_object(request.transaction_id)
        serializer = TransactionProtoSerializer(transaction, message=request)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.message

    def Destroy(self, request, context):
        transaction = self.get_object(request.transaction_id)
        transaction.delete()
        return empty_pb2.Empty()
    
    def DestroyAll(self, request, context):
        Transaction.objects.all().delete()
        return empty_pb2.Empty()
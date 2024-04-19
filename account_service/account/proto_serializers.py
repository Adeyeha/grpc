from django_grpc_framework import proto_serializers
from account.models import Account
from account_proto import account_pb2

class AccountProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Account
        proto_class = account_pb2.Account
        fields = ['account_number', 'account_type', 'currency',  'customer_id', 'balance']

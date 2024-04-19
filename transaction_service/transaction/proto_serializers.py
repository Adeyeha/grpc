from django_grpc_framework import proto_serializers
from transaction.models import Transaction
from transaction_proto import transaction_pb2


class TransactionProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Transaction
        proto_class = transaction_pb2.Transaction
        fields = ['transaction_id', 'amount', 'currency', 'dc_ind', 'description', 'date', 'account']
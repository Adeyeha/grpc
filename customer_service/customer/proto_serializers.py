from django_grpc_framework import proto_serializers
from customer.models import Customer
from customer_proto import customer_pb2


class CustomerProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Customer
        proto_class = customer_pb2.Customer
        fields = ['customer_id','first_name','last_name','email','phone_number']


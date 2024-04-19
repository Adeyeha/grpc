import grpc
from google.protobuf import empty_pb2
from django_grpc_framework.services import Service
from customer.models import Customer
from customer.proto_serializers import CustomerProtoSerializer


class CustomerService(Service):
    def List(self, request, context):
        customers = Customer.objects.all()
        serializer = CustomerProtoSerializer(customers, many=True)
        for msg in serializer.message:
            yield msg

    def Create(self, request, context):
        serializer = CustomerProtoSerializer(message=request)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.message

    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            self.context.abort(grpc.StatusCode.NOT_FOUND, 'Customer:%s not found!' % pk)

    def Retrieve(self, request, context):
        customer = self.get_object(request.customer_id)
        serializer = CustomerProtoSerializer(customer)
        return serializer.message

    def get_object_by_phone(self, phone_number):
        try:
            return Customer.objects.get(phone_number=phone_number)
        except Customer.DoesNotExist:
            self.context.abort(grpc.StatusCode.NOT_FOUND, 'Customer:%s not found!' % phone_number)

    def RetrievebyPhone(self, request, context):
        customer = self.get_object_by_phone(request.phone_number)
        serializer = CustomerProtoSerializer(customer)
        return serializer.message

    def Update(self, request, context):
        customer = self.get_object(request.customer_id)
        serializer = CustomerProtoSerializer(customer, message=request)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.message

    def Destroy(self, request, context):
        customer = self.get_object(request.customer_id)
        customer.delete()
        return empty_pb2.Empty()
    
    def DestroyAll(self, request, context):
        Customer.objects.all().delete()
        return empty_pb2.Empty()
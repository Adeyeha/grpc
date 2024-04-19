from django.shortcuts import render

# Create your views here.
# customers/views.py

from rest_framework import generics
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

class CustomerListCreate(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerByPhoneNumberRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerSerializer
    lookup_url_kwarg = 'phone_number'
    lookup_field = 'phone_number'
    queryset = Customer.objects.all()

class DeleteAllCustomers(generics.GenericAPIView):
    def delete(self, request, *args, **kwargs):
        try:
            # Delete all customer records
            Customer.objects.all().delete()
            return Response({'message': 'All customer records deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
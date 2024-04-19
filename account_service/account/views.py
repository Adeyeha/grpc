# accounts/views.py

from rest_framework import generics
from .models import Account
from .serializers import AccountSerializer
from rest_framework.response import Response
from rest_framework import status

class AccountListCreate(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountByCustomerIdRetrieveUpdateDestroy(generics.ListAPIView):
    serializer_class = AccountSerializer
    lookup_url_kwarg = 'customer_id'
    lookup_field = 'customer_id'

    def get_queryset(self):
        customer_id = self.kwargs.get(self.lookup_url_kwarg)
        queryset = Account.objects.filter(customer_id=customer_id)
        return queryset

class DeleteAllAccounts(generics.GenericAPIView):
    def delete(self, request, *args, **kwargs):
        try:
            # Delete all account records
            Account.objects.all().delete()
            return Response({'message': 'All account records deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

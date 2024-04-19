# transactions/views.py

from rest_framework import generics
from .models import Transaction
from .serializers import TransactionSerializer
from rest_framework.response import Response
from rest_framework import status

class TransactionListCreate(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class TransactionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class TransactionByAccountRetrieveUpdateDestroy(generics.ListAPIView):
    serializer_class = TransactionSerializer
    lookup_url_kwarg = 'account'
    lookup_field = 'account'

    def get_queryset(self):
        account = self.kwargs.get(self.lookup_url_kwarg)
        queryset = Transaction.objects.filter(account=account)
        return queryset

class DeleteAllTransactions(generics.GenericAPIView):
    def delete(self, request, *args, **kwargs):
        try:
            # Delete all transaction records
            Transaction.objects.all().delete()
            return Response({'message': 'All transaction records deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

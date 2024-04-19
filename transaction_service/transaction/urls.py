# transactions/urls.py

from django.urls import path
from .views import TransactionListCreate, TransactionRetrieveUpdateDestroy, DeleteAllTransactions, TransactionByAccountRetrieveUpdateDestroy

urlpatterns = [
    path('transactions/', TransactionListCreate.as_view(), name='transaction-list-create'),
    path('transactions/<int:pk>/', TransactionRetrieveUpdateDestroy.as_view(), name='transaction-retrieve-update-destroy'),
    path('transactionsbyaccount/<str:account>/', TransactionByAccountRetrieveUpdateDestroy.as_view(), name='transaction-by-account-retrieve-update-destroy'),
    path('transactions/delete-all/', DeleteAllTransactions.as_view(), name='delete-all-transactions'),
]

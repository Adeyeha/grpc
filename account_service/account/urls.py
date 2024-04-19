# accounts/urls.py

from django.urls import path
from .views import AccountListCreate, AccountRetrieveUpdateDestroy, DeleteAllAccounts, AccountByCustomerIdRetrieveUpdateDestroy

urlpatterns = [
    path('accounts/', AccountListCreate.as_view(), name='account-list-create'),
    path('accounts/<int:pk>/', AccountRetrieveUpdateDestroy.as_view(), name='account-retrieve-update-destroy'),
    path('accountsbycustomer/<str:customer_id>/', AccountByCustomerIdRetrieveUpdateDestroy.as_view(), name='account-by-customer-retrieve-update-destroy'),
    path('accounts/delete-all/', DeleteAllAccounts.as_view(), name='delete-all-accounts'),
]

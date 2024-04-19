from django.urls import path
from .views import CustomerListCreate, CustomerRetrieveUpdateDestroy, DeleteAllCustomers, CustomerByPhoneNumberRetrieveUpdateDestroy

urlpatterns = [
    path('customers/', CustomerListCreate.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerRetrieveUpdateDestroy.as_view(), name='customer-retrieve-update-destroy'),
    path('customersbyphone/<str:phone_number>/', CustomerByPhoneNumberRetrieveUpdateDestroy.as_view(), name='customer-by-phonenumber-retrieve-update-destroy'),
    path('customers/delete-all/', DeleteAllCustomers.as_view(), name='delete-all-customers'),
]


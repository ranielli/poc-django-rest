from django.urls import path
from .views import CustomerDetail, CustomerList

urlpatterns = [
    path('customers/', CustomerList.as_view(), name='customers_list'),
    path('customers/<int:pk>/', CustomerDetail.as_view(), name='customer_detail'),
]


import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Customer
from ..serializer import CustomerSerializer

# initialize the APIClient app
client = Client()


class GetAllCustomersTest(TestCase):
    """ Test module for GET all Customers API """

    def setUp(self):
        self.user_1 = Customer.objects.create(
            pk = 11, first_name='Jonh',last_name='silva Fls', email='dss@gmail.com',gender='Male',
            company='XPPP',city='Mountain View, CA',title='Dev',longitude=40.714224,latitude=-3.961452
        )
        self.user_2 = Customer.objects.create(
            pk = 13, first_name='Manoel',last_name='andreade', email='xxxxx@gmail.com',gender='Female',
            company='XPTO',city='Mountain View, CA',title='Doctor',longitude=50.714224,latitude=-73.961452
        )

    def test_get_all_customers(self):
        # get API response
        response = client.get(reverse('customers_list'))
        # get data from db
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(customers), 2)

    def test_get_valid_single_customer(self):
        response = client.get(
            reverse('customer_detail', kwargs={'pk': self.user_1.pk}))
        customer = Customer.objects.get(pk=self.user_1.pk)
        serializer = CustomerSerializer(customer)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_customer(self):
        response = client.get(
            reverse('customer_detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
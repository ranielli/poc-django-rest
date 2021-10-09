from django.test import TestCase
from ..models import Customer

# Create your tests here.
class CustomerTest(TestCase):

    def setUp(self):
        Customer.objects.create(
            pk = 11, first_name='Jonh',last_name='silva Fls', email='dss@gmail.com',gender='Male',
            company='XPTO',city='Mountain View, CA',title='Desiner',longitude=40.714224,latitude=-73.961452
        )

    def test_create_customer(self):
        customer = Customer.objects.get(pk=11)
        self.assertEqual(customer.first_name,'Jonh')
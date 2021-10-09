from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from .models import Customer
from .serializer import CustomerSerializer


class CustomerList(APIView):
    """
    API Customer List
    """
    def get(self, resquest):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

class CustomerDetail(APIView):
    """
    API Customer Retrieve
    """
    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CustomerSerializer(snippet)
        return Response(serializer.data)
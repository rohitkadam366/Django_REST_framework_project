from rest_framework import generics
from .models import Employee_generic
from api.serializers import EmployeeSerializer


# GET (list) + POST (create)
class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee_generic.objects.all()
    serializer_class = EmployeeSerializer


# GET (retrieve) + PUT (update) + DELETE (destroy)
class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee_generic.objects.all()
    serializer_class = EmployeeSerializer

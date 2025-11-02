from rest_framework import viewsets
from Employee_Generic.models import Employee_generic
from api.serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee_generic.objects.all()
    serializer_class = EmployeeSerializer

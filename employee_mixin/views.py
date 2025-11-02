from rest_framework import generics, mixins
from .models import Employee
from employee.serialization import EmployeeSerializer


# Handles GET (list) + POST (create)
class EmployeeListCreateView(mixins.ListModelMixin,
                             mixins.CreateModelMixin,
                             generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)   # from ListModelMixin

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) # from CreateModelMixin


# Handles GET (retrieve) + PUT (update) + DELETE (destroy)
class EmployeeDetailView(mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)   # from RetrieveModelMixin

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)     # from UpdateModelMixin

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)    # from DestroyModelMixin

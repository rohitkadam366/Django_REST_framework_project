from rest_framework import serializers
from student.models import Student
from Employee_Generic.models import Employee_generic


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee_generic
        fields = "__all__"



# Notes
# Without the Meta class, you'd have to manually declare every field:

# class StudentSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField(max_length=255)
#     # ...and so on

# The Meta class in Django REST Framework is what makes ModelSerializer powerful and concise. It bridges your model with the serializer — reducing boilerplate and improving clarity.
# Let me know if you want an example where Meta is extended for nested serializers or custom fields.
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *
from api.serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET','POST'])
def student(request):
    # students = {'name':"Rohit"}
    # students = Student.objects.all()
    # print(students)
    # 1.students_list = list(students.values())     # We can load by two way that is manual way that convert queryset into list,safe=False is used for if passed data is not in dict form. 
    # way 1 is not recommented way in RestFull api for fetch data , DRF provide serialization that convert complex data into json

    if request.method == "GET":
        students = Student.objects.all()
        serializer = StudentSerializer(students,many = True)        #many = True because students have multiple data

        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,JsonResponse
from .models import *
from api.serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET','POST'])
def student_view(request):
    pass
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
    


@api_view(['GET', 'PUT', 'DELETE'])
def StudentDetailsView(request,pk):
    student = get_object_or_404(Student, id=pk)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)      # here add "student" for change in that specific pk
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
from django.shortcuts import render
from rest_framework.views import APIView
from student.models import Student
from rest_framework.serializers import StudentSerializer
# from serializers import StudentSerializer

from rest_framework.response import Response
from classperiod.models import ClassPeriod
from .serializers import ClassPeriodSerializer

class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many = True)
        return Response(serializer.data)
    
class ClassPeriodListView(APIView):
    def get(self,request):
        classperiod = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(classperiod, many = True)
        return Response(serializer.data)
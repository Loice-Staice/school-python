from rest_framework import serializers
from student.models import Student
from classperiod.models import ClassPeriod
from teacher.models import Teacher
from course.models import Course
from classroom.models import Classroom

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        
class ClassroomPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model=ClassPeriod
        fields ="__all__"
        
class TeacherPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields ="__all__"
        
class CoursePeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields ="__all__"
        
class ClassroomPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model=Classroom
        fields ="__all__"
from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from student.models import Student
from .serializers import StudentSerializer
from classroom_period.models import ClassroomPeriod
from .serializers import ClassroomPeriodSerializer
from classes.models import Class
from .serializers import ClassesSerializer
from course.models import Course
from .serializers import CoursesSerializer
from teacher.models import Teacher
from .serializers import TeacherSerializer

class StudentView(APIView):
    def get(self,request):
        students = Student.objects.all()
        serializer = StudentSerializer(students,many=True)
        return Response(serializer.data)
    
class ClassroomPeriodView(APIView):
    def get(self,request):
        classperiods = ClassroomPeriod.objects.all()
        serializer = ClassroomPeriodSerializer(classperiods,many=True)
        return Response(serializer.data)
    
class ClassesView(APIView):
    def get(self,request):
        classess = Class.objects.all()
        serializer = ClassesSerializer(classess,many=True)
        return Response(serializer.data)
    
class CoursesView(APIView):
    def get(self,request):
        courses = Course.objects.all()
        serializer = CoursesSerializer(courses,many=True)
        return Response(serializer.data)
    
class TeachersView(APIView):
    def get(self,request):
        courses = Teacher.objects.all()
        serializer =TeacherSerializer(courses,many=True)
        return Response(serializer.data)
    
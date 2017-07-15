from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import *
from .serializers import *


class ListCreateStudent(viewsets.ModelViewSet):
    serializer_class = StudentSerializer

    def get_queryset(self):
        return list(map((lambda student: student.user), Student.objects.all()))


class ListCreateTeacher(generics.ListCreateAPIView):
    serializer_class = TeacherSerializer

    def get_queryset(self):
        return list(map((lambda teacher: teacher.user), Teacher.objects.all()))


class ListCreateSchool(generics.ListCreateAPIView):
    serializer_class = SchoolSerializer

    def get_queryset(self):
        return list(map((lambda school: school.user), School.objects.all()))
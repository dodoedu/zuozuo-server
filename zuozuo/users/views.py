from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import *
from .serializers import *


class ListCreateStudent(viewsets.ModelViewSet):
    serializer_class = StudentSerializer

    def get_queryset(self):
        return list(map((lambda student: student.user), Student.objects.all()))

    '''
    def perform_create(self, serializer):
        print("Creating data:")
        print(type(serializer))
        user = serializer.save()
        # user = serializer.save()
        # user = serializer.save()
        Student(user=user).save()
    '''







from rest_framework import generics
from .models import *
from .serializers import *


class ListCreateStudent(generics.ListCreateAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        return list(map((lambda student: student.user), Student.objects.all()))


class RetrieveUpdateDestroyStudent(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        # FIXME: Since it returns the user from User query directly, the following line may not needed
        student = Student.objects.get(user_id=self.kwargs.get("pk"))
        return User.objects.filter(id=self.kwargs.get("pk"))


class ListCreateTeacher(generics.ListCreateAPIView):
    serializer_class = TeacherSerializer

    def get_queryset(self):
        return list(map((lambda teacher: teacher.user), Teacher.objects.all()))


class RetrieveUpdateDestroyTeacher(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TeacherSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.kwargs.get("pk"))


class ListCreateSchool(generics.ListCreateAPIView):
    serializer_class = SchoolSerializer

    def get_queryset(self):
        return list(map((lambda school: school.user), School.objects.all()))


class RetrieveUpdateDestroySchool(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SchoolSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.kwargs.get("pk"))


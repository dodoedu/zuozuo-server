from rest_framework import generics
from . import models
from . import serializers


class ListCreateCourse(generics.ListCreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer


class RetrieveUpdateDestroyCourse(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer


class ListCreateAnnouncement(generics.ListCreateAPIView):
    queryset = models.Announcement.objects.all()
    serializer_class = serializers.AnnouncementSerializer

    def get_queryset(self):
        return self.queryset.filter(course_id=self.kwargs.get('course_pk'))


class RetrieveUpdateDestroyAnnouncement(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Announcement.objects.all()
    serializer_class = serializers.AnnouncementSerializer


class ListCreateTest(generics.ListCreateAPIView):
    queryset = models.Test.objects.all()
    serializer_class = serializers.TestSerializer

    def get_queryset(self):
        return self.queryset.filter(course_id=self.kwargs.get('course_pk'))


class RetrieveUpdateDestroyTest(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Test.objects.all()
    serializer_class = serializers.TestSerializer


class ListCreateAssignment(generics.ListCreateAPIView):
    queryset = models.Assignment.objects.all()
    serializer_class = serializers.AssignmentSerializer

    def get_queryset(self):
        return self.queryset.filter(course_id=self.kwargs.get('course_pk'))


class RetrieveUpdateDestroyAssignment(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Assignment.objects.all()
    serializer_class = serializers.AssignmentSerializer


class ListCreateResource(generics.ListCreateAPIView):
    queryset = models.Resource.objects.all()
    serializer_class = serializers.ResourceSerializer

    def get_queryset(self):
        return self.queryset.filter(course_id=self.kwargs.get('course_pk'))


class RetrieveUpdateDestroyResource(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Resource.objects.all()
    serializer_class = serializers.ResourceSerializer


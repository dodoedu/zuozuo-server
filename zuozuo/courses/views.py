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


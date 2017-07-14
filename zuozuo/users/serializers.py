from rest_framework import serializers
from . import models


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = "__all__"


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = "__all__"


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = "__all__"


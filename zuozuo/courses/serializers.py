from rest_framework import serializers

from . import models


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
            'created_at'
        )
        model = models.Course


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'created_at',
            'content',
            'course'
        )
        model = models.Announcement


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'created_at',
            'content',
            'course'
        )
        model = models.Test


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'created_at',
            'content',
            'course'
        )
        model = models.Assignment


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'created_at',
            'course'
        )
        model = models.Resource

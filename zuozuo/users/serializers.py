from django.contrib.auth.models import Group
from rest_framework import serializers
from . import models


class StudentSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        """
        Remove foreign relationships first, because relationship tables needs id, and id only will be generated after
        the user is created. So created the User first then assign  permission and groups later
        """
        data = validated_data
        data.pop("groups")
        data.pop("user_permissions")
        user = models.User.objects.create_user(**data)
        # Add user to group
        group, _ = Group.objects.get_or_create(name="student")
        group.user_set.add(user)
        # FIXME: The flowing line may not needed
        models.Student(user=user).save()
        # TODO: Add student user permission
        return user

    class Meta:
        model = models.User
        fields = "__all__"


class TeacherSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        data = validated_data
        data.pop("groups")
        data.pop("user_permissions")
        user = models.User.objects.create_user(**data)
        group, _ = Group.objects.get_or_create(name="teacher")
        group.user_set.add(user)
        # FIXME: The flowing line may not needed
        models.Teacher(user=user).save()
        return user

    class Meta:
        model = models.User
        fields = "__all__"


class SchoolSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        data = validated_data
        data.pop("groups")
        data.pop("user_permissions")
        user = models.User.objects.create_user(**data)
        group, _ = Group.objects.get_or_create(name="school")
        group.user_set.add(user)
        # FIXME: The flowing line may not needed
        models.School(user=user).save()
        return user

    class Meta:
        model = models.User
        fields = "__all__"


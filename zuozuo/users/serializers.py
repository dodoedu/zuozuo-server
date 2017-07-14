from rest_framework import serializers
from . import models


class StudentSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    def create(self, validated_data):
        """
        Remove foreign relationships first, because relationship tables needs id, and id only will be generated after
        the user is created. So created the User first then assign  permission and groups later
        """
        data = validated_data
        data.pop("groups")
        data.pop("user_permissions")
        user = models.User.objects.create_user(**data)
        models.Student(user=user).save()
        return user

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


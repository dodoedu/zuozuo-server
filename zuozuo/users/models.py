from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db import models


class User(AbstractUser):
    """Base user class, inheritances from default django user class"""
    pass


class Student(models.Model):
    """Student relation table which relates to the actual student user"""
    user = models.OneToOneField(User, related_name="student")


class Teacher(models.Model):
    """Teacher relation table which relates to the actual teacher user"""
    user = models.OneToOneField(User, related_name="teacher")

    def __init__(self):
        super().__init__()
        group, created = Group.objects.get_or_create(name="teacher")
        if created:
            course_content = ContentType.objects.get_for_model('courses.Course')
            student_content = ContentType.objects.get_for_model(Student)
            permissions = [Permission.objects.get_or_create(codename="can_manage_courses", content_type=course_content),
                           Permission.objects.get_or_create(codename="can_manage_students", content_type=student_content)]
            for p in permissions:
                group.permissions.add(p)


class School(models.Model):
    """School relation table which relates to the actual school user"""
    user = models.OneToOneField(User, related_name="school")

    def __init__(self):
        super().__init__()
        group, created = Group.objects.get_or_create(name="school")
        if created:
            course_content = ContentType.objects.get_for_model('courses.Course')
            student_content = ContentType.objects.get_for_model(Student)
            teacher_content = ContentType.objects.get_for_model(Teacher)
            permissions = [Permission.objects.get_or_create(codename="can_manage_courses", content_type=course_content),
                           Permission.objects.get_or_create(codename="can_manage_students", content_type=student_content),
                           Permission.objects.get_or_create(codename="can_manage_teachers", content_type=teacher_content)]
            group.permissions.add(permissions)
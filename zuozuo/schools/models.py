from django.db import models


class School(models.Model):
    """School model definition"""
    name = models.CharField(max_length=255)


class SchoolAdmin(models.Model):
    """School admin, multiple people are allowed for a single school"""
    name = models.CharField(max_length=255)
    school = models.ForeignKey(School, related_name="admins")


class Teacher(models.Model):
    """Teacher model definition"""
    name = models.CharField(max_length=255)
    teaching_courses = models.ManyToManyField('courses.Course')
    school = models.ForeignKey(School, related_name="teachers", null=True)


class Student(models.Model):
    """Student model definition"""
    name = models.CharField(max_length=255)
    enrolled_courses = models.ManyToManyField('courses.Course', related_name="students")


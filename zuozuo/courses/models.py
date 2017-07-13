from django.db import models


class Course(models.Model):
    """Courses definition"""
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    # school = models.ForeignKey('users.School', related_name="courses", null=True)

    def __str__(self):
        return self.title

    @classmethod
    def create(cls, **kwargs):
        """Class method responsible for creating and saving a Course object in database"""
        course = cls(**kwargs)
        course.save()
        return course


class Announcement(models.Model):
    """Course assignments"""
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    course = models.ForeignKey(Course, related_name="announcements")


class Test(models.Model):
    """Course tests"""
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    course = models.ForeignKey(Course, related_name="tests")


class Assignment(models.Model):
    """Course assignments"""
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    course = models.ForeignKey(Course, related_name="assignments")


class Resource(models.Model):
    """Course resources, for example PPT"""
    created_at = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, related_name="resources")

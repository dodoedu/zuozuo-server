from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^student/$',
        views.ListCreateStudent.as_view({
            "get": "list",
            "post": "create"
        }),
        name="student_list"),
    url(r'^teacher/$',
        views.ListCreateTeacher.as_view(),
        name="teacher_list"),
    url(r"^school/$",
        views.ListCreateSchool.as_view(),
        name="school_list")

]

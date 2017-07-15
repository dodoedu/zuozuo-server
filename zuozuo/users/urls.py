from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^student/$',
        views.ListCreateStudent.as_view(),
        name="student_list"),
    url(r"^student/(?P<pk>\d+)/$",
        views.RetrieveUpdateDestroyStudent.as_view(),
        name="student_detail"),
    url(r'^teacher/$',
        views.ListCreateTeacher.as_view(),
        name="teacher_list"),
    url(r"^teacher/(?P<pk>\d+)",
        views.RetrieveUpdateDestroyTeacher.as_view(),
        name="teacher_detail"),
    url(r"^school/$",
        views.ListCreateSchool.as_view(),
        name="school_list"),
    url(r"^school/(?P<pk>\d+)",
        views.RetrieveUpdateDestroySchool.as_view(),
        name="school_detail"),
]

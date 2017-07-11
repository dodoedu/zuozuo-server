from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',
        views.ListCreateCourse.as_view(),
        name="course_list"),
    url(r'(?P<pk>\d+)/$',
        views.RetrieveUpdateDestroyCourse.as_view(),
        name="course_detail"),
    url(r'^(?P<course_pk>\d+)/ann/$',
        views.ListCreateAnnouncement.as_view(),
        name="announcement_list"),
    url(r'^(?P<course_pk>\d+)/ann/(?P<pk>\d+)/$',
        views.RetrieveUpdateDestroyAnnouncement.as_view(),
        name="announcement_detail"),
    url(r'^(?P<course_pk>\d+)/test/$',
        views.ListCreateTest.as_view(),
        name="test_list"),
    url(r'^(?P<course_pk>\d+)/test/(?P<pk>\d+)/$',
        views.RetrieveUpdateDestroyTest.as_view(),
        name="test_detail"),
    url(r'^(?P<course_pk>\d+)/ass/$', views.ListCreateAssignment.as_view(),
        name="assignment_list"),
    url(r'^(?P<course_pk>\d+)/ass/(?P<pk>\d+)/$',
        views.RetrieveUpdateDestroyAssignment.as_view(),
        name="assignment_detail"),
    url(r'^(?P<course_pk>\d+)/resource/$',
        views.ListCreateResource.as_view(),
        name="resource_list"),
    url(r'^(?P<course_pk>\d+)/resource/(?P<pk>\d+)/$',
        views.RetrieveUpdateDestroyResource.as_view(),
        name="resource_detail")
]

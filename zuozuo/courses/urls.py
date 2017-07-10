from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ListCreateCourse.as_view(), name="course_list"),
    url(r'(?P<pk>\d+)/$', views.RetrieveUpdateDestroyCourse.as_view(), name="course_detail"),
    url(r'^(?P<course_pk>\d+)/ann/$', views.ListCreateAnnouncement.as_view(),
        name="announcement_list"),
    url(r'^(?P<course_pk>\d+)/ann/(?P<pk>\d+)/$',
        views.RetrieveUpdateDestroyAnnouncement.as_view(),
        name="announcement_detail")
]

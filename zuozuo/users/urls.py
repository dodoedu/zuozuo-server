from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^student/$',
        views.ListCreateStudent.as_view({
            "get": "list",
            "post": "create"
        }),
        name="student_list"),
]

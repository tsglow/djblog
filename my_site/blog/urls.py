from django.urls import path
from . import views

urlpatterns = [    
    path("", views.index, name="index"),
    path("<slug:url>", views.read_post, name="read-post")
]

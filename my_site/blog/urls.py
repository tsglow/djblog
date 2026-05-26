from django.urls import path
from . import views

urlpatterns = [    
    path("", views.index, name="index"),
    path("tag/<str:url>", views.tags, name="tags"),
    path("posts", views.posts, name="posts"),
    path("posts/<slug:url>", views.read_post, name="read-post"),
    
]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("posts/<int:pk>/", views.post_detail, name="post_detail"),
    path("posts/new/", views.PostCreateView.as_view(), name="post_create"),
    path("posts/<int:pk>/edit/", views.PostUpdateView.as_view(), name="post_edit"),
    path("posts/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post_delete"),
]

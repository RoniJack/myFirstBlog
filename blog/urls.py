from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('posts/', views.posts,name="all-posts"),
    path('posts/<slug:slug>', views.single_post ,name="dataPost")
]

from django.urls import path

from . import views

urlpatterns = [
    path('post/', views.posts_list, name='posts_list'),
]
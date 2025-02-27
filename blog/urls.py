from django.urls import path
from .views import post_list
from . import views

urlpatterns = [
    path('', post_list, name='post_list'),
    path('add/', views.add_post, name='add_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
]


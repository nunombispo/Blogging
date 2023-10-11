from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_post, name='create_post'),
    path('register/', views.register, name='register'),  # New URL pattern for registration
    path('', views.post_list, name='post_list'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),  # New URL pattern for post details
    path('<slug:slug>/delete/', views.delete_post, name='delete_post'),
]

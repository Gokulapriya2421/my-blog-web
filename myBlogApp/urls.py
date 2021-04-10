from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

]
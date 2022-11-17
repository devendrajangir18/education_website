from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('postblog/', views.post_comment, name='post_comment'),
    path('postblog/<post_id>', views.post_comment, name='post_comment'),
]
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [   
    path('post/', views.postcommit, name='postcommit'),
    path("post/<post_id>", views.post_page, name="post_page")
    
    ]
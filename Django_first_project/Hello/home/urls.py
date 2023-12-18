from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path("",views.index,name="home"),
    path("about",views.about,name="about"),
    path("services",views.services,name="services"),
    path("project",views.services,name="project"),
    path("contect",views.contect,name="contect"),
]

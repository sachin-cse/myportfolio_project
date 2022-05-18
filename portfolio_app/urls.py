from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name = "home"),
    path('about-us/',views.about,name = "about"),
    path('contact-us/',views.contact,name = "contact"),
    path('resume/',views.resume,name = "Resume"),
    path('message/',views.message,name = "message"),
]
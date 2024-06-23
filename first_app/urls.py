from django.urls import path
from . import views

urlpatterns = [
    path("courses/", views.courses),
    path("about/", views.about),
    path("contact/", views.contact),
    path("", views.home),
]
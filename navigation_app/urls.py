from django.urls import path, include
# from views import contact
from . import views

urlpatterns = [
    path('about/', views.about),
    path('contact/', views.contact),
]
from django.contrib import admin
from django.urls import path, include
# from views import contact
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', views.contact),
    path('', views.home),
    # path('', views.index),
    # All the urls of first_app will start by first_app/
    path('first_app/', include("first_app.urls")),
    path('second_app/', include("second_app.urls")),
    path('navigation_app/', include('navigation_app.urls'))
]
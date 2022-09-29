from django.urls import path
from . import views

urlpatterns = [ #ip주소/
    path('', views.landing),
    path('about_me/', views.about_me)
    ]
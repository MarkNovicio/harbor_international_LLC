from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('user/registration', views.create_registration),
    path('user/login', views.login_page),
    path('user/logout', views.logout)
]
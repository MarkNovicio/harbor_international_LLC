from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('user/signup', views.signup),
    path('user/registration', views.create_registration),
    path('user/login', views.login),
    path('user/login_page', views.login_page),
    path('user/logout', views.logout)
]
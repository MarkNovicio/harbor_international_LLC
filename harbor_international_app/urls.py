from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('math/courses', views.math_courses)

]
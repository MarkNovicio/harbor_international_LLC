from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('courses', views.courses),
    path('courses/content', views.video),
    path('admin', views.admin)

]
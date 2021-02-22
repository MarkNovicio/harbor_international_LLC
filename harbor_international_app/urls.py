from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('courses', views.courses),
    path('courses/content', views.video),
    path('videos/<int:video_id>/delete', views.delete_video),
    path('admin', views.admin),
    path('video_form', views.videoForm),
    path('upload/video', views.uploadvideo),
    path('upload/algebra', views.uploadalgebra),
    path('upload/geometry', views.uploadgeometry),
    path('courses/<int:course_id>/geometry', views.geometry_material)
   #path('courses/<str:course_id>', views.course_material)

    #path('video/upload', views.upload)
]
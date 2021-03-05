from django.db import models
from embed_video.fields import EmbedVideoField
#from .validators import file_size

class Item(models.Model):
    video = EmbedVideoField()  # same like models.URLField()

class Video(models.Model):
    caption = models.CharField(max_length=50)
    content= models.CharField(max_length=3000)
    videofile =models.FileField(upload_to="videos/", null=True, verbose_name="")
    def __str__(self):
        return self.caption + ":" + str(self.videofile)

class Algebra(models.Model):
    caption = models.CharField(max_length=50)
    content= models.TextField(max_length=3000)
    videofile =models.FileField(upload_to="algebra/", null=True, verbose_name="")
    def __str__(self):
        return self.caption + ":" + str(self.videofile)

class Geometry(models.Model):
    caption = models.CharField(max_length=50)
    content= models.TextField(max_length=3000)
    videofile =models.FileField(upload_to="geometry/", null=True, verbose_name="")
    def __str__(self):
        return self.caption + ":" + str(self.videofile)



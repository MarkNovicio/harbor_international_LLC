from django.db import models
from embed_video.fields import EmbedVideoField
from .validaotrs import files_size

class Item(models.Model):
    caption = models.CharField(max_length=100)
    video = EmbedVideoField()  # same like models.URLField()

class Video(models.Model):
    caption = models.CharField(max_length=50)
    content= models.CharField()
    video =models.FileField(upload_to="video/%y", validators=[file_size])
    def __str__(self):
        return self.caption


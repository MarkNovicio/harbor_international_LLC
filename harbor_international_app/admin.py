from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Item, Video

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Item, MyModelAdmin)

admin.site.register(Video)
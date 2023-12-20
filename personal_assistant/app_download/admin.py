from django.contrib import admin
from .models import File, Photo, Music, Video, Other

# Register your models here.
admin.site.register(File)
admin.site.register(Photo)
admin.site.register(Music)
admin.site.register(Video)
admin.site.register(Other)
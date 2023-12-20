import os
from uuid import uuid4

from django.db import models
from django.contrib.auth.models import User

EXTENSIONS = {'video':['mp4', 'mov', 'wmv', 'avi', 'avchd', 'flv', 'f4v', 'swf', 'mkv'],
              'audio':['mp3', 'aac', 'aiff', 'dsd', 'flac', 'mqa', 'ogg', 'wav'],
              'image':['bmp', 'ecw', 'gif', 'ico', 'ilbm', 'jpeg', 'jpeg2000', 'pcx', 'png', 'psd', 'tga', 'tiff', 'jfif'],
              'documents':['doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'txt', 'pdf', 'rar', 'zip', 'jar', '7z', 'gz']
             }


def update_filename(instance, filename):
    upload_file = 'other'
    #upload_file_music = 'music'
    file_ext = filename.split('.')[-1]
    filename = f"{uuid4().hex}.{file_ext}"
    for k,v in EXTENSIONS.items():
        if file_ext in v:
            return os.path.join(k, filename)
    return os.path.join(upload_file, filename)


class File(models.Model):
    description = models.CharField(max_length=150, null=True)
    path = models.FileField(upload_to=update_filename)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)



def update_photoname(instance, photoname):
    upload_photo = 'photo'
    file_ext = photoname.split('.')[-1]
    photoname = f"{uuid4().hex}.{file_ext}"
    return os.path.join(upload_photo, photoname)


class Photo(models.Model):
    description = models.CharField(max_length=150, null=True)
    path = models.FileField(upload_to=update_photoname)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


def update_musicname(instance, musicname):
    upload_music = 'music'
    file_ext = musicname.split('.')[-1]
    musicname = f"{uuid4().hex}.{file_ext}"
    return os.path.join(upload_music, musicname)


class Music(models.Model):
    description = models.CharField(max_length=150, null=True)
    path = models.FileField(upload_to=update_musicname)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


def update_videoname(instance, videoname):
    upload_video = 'video'
    file_ext = videoname.split('.')[-1]
    videoname = f"{uuid4().hex}.{file_ext}"
    return os.path.join(upload_video, videoname)


class Video(models.Model):
    description = models.CharField(max_length=150, null=True)
    path = models.FileField(upload_to=update_videoname)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


def update_othername(instance, othername):
    upload_other = 'other'
    file_ext = othername.split('.')[-1]
    othername = f"{uuid4().hex}.{file_ext}"
    return os.path.join(upload_other, othername)


class Other(models.Model):
    description = models.CharField(max_length=150, null=True)
    path = models.FileField(upload_to=update_othername)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
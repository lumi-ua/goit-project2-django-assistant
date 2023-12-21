import os
from uuid import uuid4

from django.db import models
from django.contrib.auth.models import User
from pathlib import Path

##########################################################
img_f = {'.jpeg', '.png', '.jpg', '.svg', ".bmp", ".ico"}
mov_f = {'.avi', '.mp4', '.mov', '.mkv', ".webm", ".wmv", ".flv"}
doc_f = {'.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx', ".ini", ".cmd", ".ppt", ".xml", ".msg", ".cpp", ".hpp", ".py", ".md"}
mus_f = {'.mp3', '.ogg', '.wav', '.amr', ".aiff"}
arch_f = {'.zip', '.tar'}

##########################################################
CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

CATEGORIES = { 
    "image" : img_f, 
    "video" : mov_f, 
    "document" : doc_f, 
    "music" : mus_f,
    "archives" : arch_f,
}

###########################################################
def getCategory(suffix: str):
    TRANS = {}
    for c, t in zip(CYRILLIC_SYMBOLS, TRANSLATION):
       TRANS[ord(c)] = t
       TRANS[ord(c.lower())] = t.lower()
    #####################################

    for cat, exts in CATEGORIES.items():
        if suffix in exts:
            return cat
    return "others"
###########################################################


def update_filename(instance, filename):
    pathfile = Path(filename)
    filename = f"{uuid4().hex}.{pathfile.name}"
    category_id = str(getCategory(pathfile.suffix))
    return os.path.join(category_id, filename)

class File(models.Model):
    CATEGORY = (
        ('video', ('Video')),
        ('image', ('Image')),
        ('document', ('Document')),
        ('music', ('Music')),
        ('other', ('Other')),
    )
    description = models.CharField(max_length=150, null=True)
    path = models.FileField(upload_to=update_filename)
    category = models.CharField('File Category', max_length=40, choices=CATEGORY, default='other')
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
    category_dir = ""
    file_ext = othername.split('.')[-1]
    othername = f"{uuid4().hex}.{file_ext}"
    return os.path.join(category_dir, othername)


class Other(models.Model):
    description = models.CharField(max_length=150, null=True)
    path = models.FileField(upload_to=update_othername)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
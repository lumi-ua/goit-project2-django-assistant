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

def getCategory_str(filename):
    suffix = Path(filename).suffix
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
    category_id = getCategory_str(pathfile.name)
    return os.path.join(category_id, filename)

class File(models.Model):
    description = models.CharField(max_length=150, null=True)
    path = models.FileField(upload_to=update_filename)
    category = models.CharField('File Category', max_length=40, default='other')
    original_name = models.CharField(max_length=255, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def save(self, **kwargs):
        self.category = getCategory_str(self.path.name)
        super().save(**kwargs)


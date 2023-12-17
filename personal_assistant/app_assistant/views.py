from storages.backends.dropbox import DropboxStorage
from dropbox.files import WriteMode
from django.conf import settings
from django.shortcuts import render

def main(request):
    return render(request, 'app_assistant/index.html')

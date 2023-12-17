from storages.backends.dropbox import DropboxStorage
from dropbox.files import WriteMode
from .forms import FileUploadForm
import os

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .forms import PictureForm
from .models import Picture
from decouple import config

DROPBOX_OAUTH2_TOKEN = config('DROPBOX_OAUTH2_TOKEN')


def main(request):
    return render(request, 'app_storage/index.html')


@login_required
def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file_instance = form.save(commit=False)
            file_instance.save()
            dbx = DropboxStorage(token=DROPBOX_OAUTH2_TOKEN)
            mode = WriteMode.overwrite
            data = "Your data here"
            name = "YourFileName.txt"
            dbx.client.files_upload(bytes(data, 'utf-8'), name, mode)

            return render(request, 'success.html')
    else:
        form = FileUploadForm()
    return render(request, 'app_storage/dropbox.html', {'form': form})


@login_required
def upload(request):
    form = PictureForm(instance=Picture())
    if request.method == "POST":
        form = PictureForm(request.POST, request.FILES, instance=Picture())
        if form.is_valid():
            pic = form.save(commit=False)
            pic.user = request.user
            pic.save()
            return redirect(to="app_storage:pictures")
    return render(request, 'app_storage/upload.html', context={"title": "Group 6", "form": form})


@login_required
def pictures(request):
    pictures = Picture.objects.filter(user=request.user).all()
    return render(request, 'app_storage/pictures.html',
                  context={"title": "Group 6", "pictures": pictures, "media": settings.MEDIA_URL})


@login_required
def remove(request, pic_id):
    picture = Picture.objects.filter(pk=pic_id, user=request.user)
    try:
        os.unlink(os.path.join(settings.MEDIA_ROOT, str(picture.first().path)))
    except OSError as e:
        print(e)
    picture.delete()
    return redirect(to="app_storage:pictures")

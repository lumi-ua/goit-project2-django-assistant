from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .forms import FileForm
from .models import File, update_filename


def search_by_category(request, category: str):
    result = None
    try:
        files = File.objects.filter(user=request.user)
        result = files.filter(Q(category=category))

    except File.DoesNotExist:
        result = []
    return result
##############################################

# Create your views here.
@login_required
def main(request):
    return render(request, 'app_download/index.html', context={"title": "DownLoad"})


@login_required
def upload(request):
    form = FileForm(instance=File())
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES, instance=File())
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect(to="app_download:files")
    return render(request, 'app_download/upload.html', context=
        {
            "title": "DownLoad",
            "form": form,
            "media": settings.MEDIA_URL
        })

@login_required
def files(request):
    files = File.objects.filter(user=request.user)
    return render(request, 'app_download/files.html', context=
        {
            "title": "DownLoad",
            "files": files,
            "media": settings.MEDIA_URL
        })

@login_required
def images(request):
    category = "image"
    image_list = search_by_category(request, category)
    return render(request, 'app_download/image.html', context=
        {
            "title": "DownLoad", 
            "image_list": image_list,
            "media": settings.MEDIA_URL
        })

@login_required
def documents(request):
    category = "document"
    document_list = search_by_category(request, category)
    return render(request, 'app_download/document.html', context=
        {
            "title": "DownLoad",
            "document_list": document_list,
            "media": settings.MEDIA_URL
        })

@login_required
def videos(request):
    category = "video"
    video_list = search_by_category(request, category)
    return render(request, 'app_download/video.html', context=
        {
            "title": "DownLoad",
            "video_list": video_list,
            "media": settings.MEDIA_URL
        })

@login_required
def musics(request):
    category = "music"
    music_list = search_by_category(request, category)
    return render(request, 'app_download/music.html', context=
        {
            "title": "DownLoad",
            "music_list": music_list,
            "media": settings.MEDIA_URL
        })

@login_required
def archives(request):
    category = "archive"
    archive_list = search_by_category(request, category)
    return render(request, 'app_download/archive.html', context=
        {
            "title": "DownLoad",
            "archive_list": archive_list,
            "media": settings.MEDIA_URL
        })

@login_required
def others(request):
    category = "other"
    other_list = search_by_category(request, category)
    return render(request, 'app_download/other.html', context=
        {
            "title": "DownLoad", 
            "other_list": other_list,
            "media": settings.MEDIA_URL
        })


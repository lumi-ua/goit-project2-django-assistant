from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db import IntegrityError
from django.shortcuts import render, redirect

from .models import Tag, Note



@login_required
def main(request):
    notes = Note.objects.filter(author=request.user).all()
    paginator = Paginator(notes, 5)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'note_app/index.html', {"page_obj": page_obj})


@login_required
def tag(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            if name:
                tl = Tag(name=name, author=request.user)
                tl.save()
                messages.success(request, f"Tag {name} created")
            return redirect(to='/note_app/tag/')
        except ValueError as err:
            messages.error(request, err)
            return render(request, 'note_app/tag.html', {"error": err})
        # except IntegrityError as err:
        except IntegrityError:
            err = "Tag is exist, try enter another tag..."
            messages.error(request, err)
            return render(request, 'note_app/tag.html', {"error": err})
    return render(request, 'note_app/tag.html', {})


@login_required
def note(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        list_tags = request.POST.getlist('tags')
        if name and description:
            tags = Tag.objects.filter(name__in=list_tags).filter(author=request.user).all()
            note = Note.objects.create(name=name, description=description, author=request.user)
            for tag in tags.iterator():
                note.tags.add(tag)
            messages.success(request, f"Note {name} created")
        return redirect(to='/note_app/note/')

    tags = Tag.objects.filter(author=request.user).all()
    return render(request, 'note_app/note.html', {"tags": tags})


@login_required
def detail(request, note_id):
    note = Note.objects.get(pk=note_id)
    note.tag_list = ', '.join([str(name) for name in note.tags.all()])
    return render(request, 'note_app/detail.html', {"note": note})


@login_required
def set_done(request, note_id):
    Note.objects.filter(pk=note_id).update(done=True)
    return redirect(to='/note_app/')


@login_required
def delete_note(request, note_id):
    note = Note.objects.get(pk=note_id)
    note.delete()
    return redirect(to='/note_app/')


@login_required
def search_note(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        notes = Note.objects.filter(name__icontains=query, author=request.user)
    else:
        notes = []
    return render(request, 'note_app/search_note.html', {'notes': notes})
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Tag, Note
from .forms import NoteForm

@login_required
def main(request):
    """
    Main function for displaying the main notes page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: A response with the index.html template rendered with the page context.

    """
    # Get all notes for the current user
    notes = Note.objects.filter(author=request.user).all()

    # Create a paginator object with a page size of 5 notes per page
    paginator = Paginator(notes, 5)

    # Get the page number from the request's GET parameters
    page_number = request.GET.get("page")

    # Retrieve the page object based on the page number
    page_obj = paginator.get_page(page_number)
    #
    # index_url = reverse('app_notes:index')  # 'app_notes' - ім'я вашої додаткової аплікації

    # Render the index.html template with the page object as context
    return render(request, "app_notes/index.html", {"page_obj": page_obj})


@login_required
def tag(request):
    """
    View function to handle tag creation.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.

    Raises:
        ValueError: If there is an error in the tag creation process.

    """
    if request.method == "POST":
        try:
            name = request.POST["name"]

            if name:
                tl = Tag(name=name, author=request.user)
                tl.save()
                messages.success(request, f"Tag {name} created")

            return redirect(to="/app_notes/tag/")

        except ValueError as err:
            messages.error(request, err)
            return render(request, "app_notes/tag.html", {"error": err})

        except IntegrityError:
            err = "Tag already exists, please enter another tag..."
            messages.error(request, err)
            return render(request, "app_notes/tag.html", {"error": err})

    return render(request, "app_notes/tag.html", {})


@login_required
def note(request):
    """
    View function for creating a new note or rendering the note form.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponseRedirect or HttpResponse: The response object.

    Raises:
        None
    """
    if request.method == "POST":
        # Get the name, description, and tags from the POST request
        name = request.POST["name"]
        description = request.POST["description"]
        list_tags = request.POST.getlist("tags")

        if name and description:
            # Filter the tags based on name and author
            tags = (
                Tag.objects.filter(name__in=list_tags).filter(author=request.user).all()
            )

            # Create a new note with the given name, description, and author
            note = Note.objects.create(
                name=name, description=description, author=request.user
            )

            # Add the filtered tags to the note
            for tag in tags.iterator():
                note.tags.add(tag)

            # Display a success message
            messages.success(request, f"Note {name} created")

        return redirect(to="/app_notes/note/")

    # Get all tags for the current user
    tags = Tag.objects.filter(author=request.user).all()

    # Render the note form with the tags
    return render(request, "app_notes/note.html", {"tags": tags})


@login_required
def detail(request, note_id):
    """
    Retrieves the note with the given note_id from the database,
    generates a comma-separated string of tag names associated with the note,
    and renders the detail.html template with the note object as context.

    Args:
        request (HttpRequest): The HTTP request object.
        note_id (int): The ID of the note to retrieve.

    Returns:
        HttpResponse: The rendered detail.html template with the note object as context.
    """
    # Retrieve the note with the given note_id from the database
    note = Note.objects.get(pk=note_id)

    # Generate a comma-separated string of tag names associated with the note
    note.tag_list = ", ".join([str(name) for name in note.tags.all()])

    # Render the detail.html template with the note object as context
    return render(request, "app_notes/detail.html", {"note": note})


@login_required
def set_done(request, note_id):
    """
    View function to set a note as done.

    Args:
        request (HttpRequest): The HTTP request object.
        note_id (int): The ID of the note to set as done.

    Returns:
        HttpResponseRedirect: A redirect response to the note app home page.
    """
    Note.objects.filter(pk=note_id).update(done=True)
    return redirect(to="/app_notes/")


@login_required
def delete_note(request, note_id):
    """
    Delete a note with the given note_id.

    Args:
        request (HttpRequest): The HTTP request object.
        note_id (int): The ID of the note to delete.

    Returns:
        HttpResponseRedirect: A redirect response to the note app homepage.
    """
    note = Note.objects.get(pk=note_id)  # Get the note with the given note_id
    note.delete()  # Delete the note
    return redirect(to="/app_notes/")  # Redirect to the note app homepage


@login_required
def search_note(request):
    """
    View function to search for notes.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered template.

    """
    if request.method == "GET":
        query = request.GET.get("q")  # Get the query parameter from the request
        notes = Note.objects.filter(
            name__icontains=query, author=request.user
        )  # Filter notes by name and author
    else:
        notes = []  # Set notes to an empty list if the request method is not GET

    return render(
        request, "app_notes/search_note.html", {"notes": notes}
    )  # Render the template with the notes as
    # context

@login_required
def edit_note(request, note_id):
    try:
        note = Note.objects.get(pk=note_id, author=request.user)
        if request.method == "POST":
            form = NoteForm(request.POST, instance=note)
            if form.is_valid():
                form.save()
                messages.success(request, f"Note '{note.name}' updated successfully")
                return redirect('app_notes:detail', note_id=note_id)
        else:
            form = NoteForm(instance=note)
        return render(request, 'app_notes/edit_note.html', {'form': form, 'note_id': note_id})
    except Note.DoesNotExist:
        messages.error(request, "Note does not exist or you don't have permission to edit it")
        return redirect('app_notes:detail', note_id=note_id)
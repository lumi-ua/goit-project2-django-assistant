from datetime import date, datetime, timedelta
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from django.http import HttpResponseBadRequest

from .forms import ContactForm
from .models import Contact

# Create your views here.



def contact(request):
    form = ContactForm()  
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            new_contact = form.save()
            new_contact.save()
            return redirect(to="app_assistant:main")   
    else:
        return render(
            request,
            "app_contacts/contact.html",
            {"form": form},
        ) 
    return render(
        request,
        "app_contacts/contact.html",
        {"form": ContactForm()},
    )  

def contacts(request):
    contacts = Contact.objects.all()
    return render(request, "app_contacts/all_contacts.html", {"contacts": contacts})


def upcoming_birthdays(request):
    today = date.today()
    days_in_future = int(request.GET.get("days", 7))

    contacts = Contact.objects.filter(
        birthday__month__gte=today.month,
        birthday__day__lte=today.day + days_in_future,        
    )
    if not contacts.exists():
        return render(request, "app_contacts/upcoming_birthdays.html", {"message": "No upcoming birthdays."})
    
    return render(request, "app_contacts/upcoming_birthdays.html", {"contacts": contacts})

    

def search_contacts(request):
    query = request.GET.get("query", "")
    error_message = ""
    

    try:
        contacts = Contact.objects.filter(
            Q(fullname__icontains=query)
            | Q(phone_number__icontains=query)
            | Q(email__icontains=query)
        )
    except Contact.DoesNotExist:
        contacts = []
        error_message = "Контакт не знайдено"
        

    return render(request, "app_contacts/search_contacts.html", {"contacts": contacts, "error_message": error_message})





# def edit_contact(request, pk):
#     contact = get_object_or_404(Contact, pk=pk)

#     if request.method == "POST":
#         form = ContactForm(request.POST, instance=contact)
#         if form.is_valid():
#             form.save()
#             return redirect('app_assistant:main')
#             # return redirect('app_contacts:contact_detail', pk=pk)
            
#     else:
#         form = ContactForm(instance=contact)

#     return render(request, 'app_contacts/edit_contact.html', {'form': form, 'contact': contact})

def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    birthday_str = ''
    

    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('app_assistant:main')

    else:
        form = ContactForm(instance=contact)
        if request.method == "POST":
            birthday_str = contact.birthday.as_formatted_str("%d.%m.%Y")

    return render(request, 'app_contacts/edit_contact.html', {'form': form, 'contact': contact, 'birthday_str': birthday_str})



def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)

    if request.method == 'POST':
        contact.delete()
        return redirect('app_contacts:main')

    return render(request, 'app_contacts/delete_contact.html', {'contact': contact})


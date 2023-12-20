from datetime import date, timedelta, datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.urls import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.utils import timezone

from .forms import ContactForm, PhoneNumberForm, EmailAddressForm
from .models import Contact, PhoneNumber, EmailAddress

# Create your views here.

@login_required
def dashboard(request):
    return render(request, 'app_contacts/dashboard.html')


@login_required
def contact(request):
    contact_form = ContactForm()
    phone_number_form = PhoneNumberForm()
    email_address_form = EmailAddressForm()

    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        phone_number_form = PhoneNumberForm(request.POST)
        email_address_form = EmailAddressForm(request.POST)

        if contact_form.is_valid() and phone_number_form.is_valid() and email_address_form.is_valid():
            new_contact = contact_form.save(commit=False)
            new_contact.user = request.user
            new_contact.save()

            phone_number = phone_number_form.save(commit=False)
            phone_number.contact = new_contact
            phone_number.save()

            email_address_data = email_address_form.cleaned_data
            if email_address_data.get("email"):
                email_address = email_address_form.save(commit=False)
                email_address.contact = new_contact
                email_address.save()

            return redirect(to="app_contacts:dashboard")

    return render(
        request,
        "app_contacts/contact.html",
        {
            "contact_form": contact_form,
            "phone_number_form": phone_number_form,
            "email_address_form": email_address_form,
        },
    )


@login_required
def contacts(request, page=1):
    per_page = 10
    contacts = Contact.objects.filter(user=request.user)
    paginator = Paginator(list(contacts), per_page)
    contacts_on_page = paginator.page(page)
    return render(request, "app_contacts/all_contacts.html", {"contacts": contacts_on_page})


@login_required
def detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'app_contacts/detail.html', {'contact': contact})


@login_required
def add_phone_number(request, pk):
    contact = Contact.objects.get(pk=pk)
    phone_number_add_url = reverse_lazy('app_contacts:add_phone_number', kwargs={'pk': pk})
    if request.method == 'POST':
        phone_number_form = PhoneNumberForm(request.POST)
        if phone_number_form.is_valid():
            new_phone_number = phone_number_form.save()
            new_phone_number.contact = contact
            new_phone_number.save()
            return redirect(to="app_contacts:detail", pk=pk)
           
    else:
        phone_number_form = PhoneNumberForm()
        

    return render(request, 'app_contacts/add_phone_number.html', {
        'phone_number_form': phone_number_form,
        'phone_number_add_url': phone_number_add_url,
    })


@login_required
def add_email_address(request, pk):
    contact = Contact.objects.get(pk=pk)
    email_adress_add_url = reverse_lazy('app_contacts:add_email_address', kwargs={'pk': pk})
    if request.method == 'POST':
        email_address_form = EmailAddressForm(request.POST)
        if email_address_form.is_valid():
            new_email_address = email_address_form.save()
            new_email_address.contact = contact
            new_email_address.save()
            return redirect(to="app_contacts:detail", pk=pk)
    else:
        email_address_form = EmailAddressForm()

    return render(request, 'app_contacts/add_email_address.html', 
                  {
                    'email_address_form': email_address_form,
                    'email_adress_add_url': email_adress_add_url
                    })


@login_required
def upcoming_birthdays(request):
    today = date.today()
    days_in_future = int(request.GET.get("days", 7))

    future_date = today + timedelta(days=days_in_future)

    contacts = Contact.objects.filter(
        birthday__month=today.month,
        birthday__day__gte=today.day + future_date,
        # birthday__day__lte=future_date,
        user=request.user,
    )

    if not contacts.exists():
        return render(request, "app_contacts/upcoming_birthdays.html", {"message": "No upcoming birthdays."})

    return render(request, "app_contacts/upcoming_birthdays.html", {"contacts": contacts})



@login_required
def search_contacts(request):
    query = request.GET.get("query", "")
    error_message = ""

    try:
        user_contacts = Contact.objects.filter(user=request.user)
        contacts = user_contacts.filter(
            Q(fullname__icontains=query)
            | Q(phone_numbers__phone_number__icontains=query)
            | Q(email_addresses__email__icontains=query)
        ).distinct()
    except Contact.DoesNotExist:
        contacts = []
        error_message = "Сontact not found"

    return render(request, "app_contacts/search_contacts.html", {"contacts": contacts, "error_message": error_message})




@login_required
def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect(to="app_contacts:detail", pk=pk)
    else:
        form = ContactForm(instance=contact)
        

    return render(request, 'app_contacts/edit_contact.html', {'form': form, 'contact': contact})



@login_required
def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)

    if request.method == "POST":
        contact.delete()
        messages.success(request, "Контакт успешно удален")
        return redirect(to="app_contacts:dashboard")

    else:
        return render(request, "app_contacts/delete_contact.html", {"contact": contact, "user": request.user})
    


def delete_email(request, pk):
    try:
        email = EmailAddress.objects.get(pk=pk)
        email.delete()
    except ObjectDoesNotExist:
        email = None

    return detail(request, pk)


def delete_phone(request, pk):
    try:
        phone = PhoneNumber.objects.get(pk=pk)
        phone.delete()
    except ObjectDoesNotExist:
        phone = None

    return detail(request, pk)

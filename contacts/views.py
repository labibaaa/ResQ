from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import EmergencyContact
from .forms import EmergencyContactForm


def contacts_page(request):
    contacts = EmergencyContact.objects.filter(
        is_active=True
    ).order_by('category', 'name')
    grouped = {}
    for contact in contacts:
        grouped.setdefault(contact.get_category_display(), []).append(contact)
    return render(request, 'contacts/contacts.html', {'grouped': grouped})


@login_required
def contact_create(request):
    if request.user.role != 'authority':
        return redirect('contacts_page')
    if request.method == 'POST':
        form = EmergencyContactForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.added_by = request.user
            obj.save()
            return redirect('contacts_page')
    else:
        form = EmergencyContactForm()
    return render(request, 'contacts/edit.html', {'form': form})


@login_required
def contact_edit(request, pk):
    if request.user.role != 'authority':
        return redirect('contacts_page')
    contact = get_object_or_404(EmergencyContact, pk=pk)
    if request.method == 'POST':
        form = EmergencyContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contacts_page')
    else:
        form = EmergencyContactForm(instance=contact)
    return render(request, 'contacts/edit.html', {'form': form})


from django.shortcuts import render

# Create your views here.

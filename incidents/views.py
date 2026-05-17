from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import IncidentReportForm
from .models import Incident
from users.models import User


def report_incident(request):
    if request.method == 'POST':
        form = IncidentReportForm(request.POST)
        if form.is_valid():
            incident = form.save()
            return redirect(f'/guide/#{incident.emergency_type}')
        from mysite.views import get_home_context
        return render(request, 'home.html', get_home_context(form=form))
    return redirect('home')


@login_required
def incident_list(request):
    user = request.user
    if user.role == 'authority':
        incidents = Incident.objects.all().order_by('-reported_at')
    else:
        incidents = Incident.objects.filter(
            assigned_volunteer=user
        ).order_by('-reported_at')
    return render(request, 'incidents/list.html', {'incidents': incidents})


@login_required
def incident_detail(request, pk):
    incident = get_object_or_404(Incident, pk=pk)
    volunteers = None
    if request.user.role == 'authority':
        volunteers = User.objects.filter(role='volunteer', is_active=True).order_by('username')
    return render(request, 'incidents/detail.html', {
        'incident': incident,
        'volunteers': volunteers,
    })


@login_required
def assign_volunteer(request, pk):
    if request.user.role != 'authority':
        return redirect('dashboard')
    incident = get_object_or_404(Incident, pk=pk)
    if request.method == 'POST':
        volunteer_id = request.POST.get('volunteer_id')
        if volunteer_id:
            volunteer = get_object_or_404(User, pk=volunteer_id, role='volunteer')
            incident.assigned_volunteer = volunteer
            if incident.status == 'pending':
                incident.status = 'active'
            incident.save()
        else:
            incident.assigned_volunteer = None
            incident.save()
    return redirect('incident_detail', pk=pk)


@login_required
def resolve_incident(request, pk):
    if request.user.role != 'authority':
        return redirect('dashboard')
    incident = get_object_or_404(Incident, pk=pk)
    incident.status = 'resolved'
    incident.resolved_at = timezone.now()
    incident.save()
    return redirect('incident_list')

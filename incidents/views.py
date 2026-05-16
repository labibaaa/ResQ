from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import IncidentReportForm
from .models import Incident


def report_incident(request):
    if request.method == 'POST':
        form = IncidentReportForm(request.POST)
        if form.is_valid():
            incident = form.save()
            # redirect to guide section matching the emergency type
            emergency_type = incident.emergency_type
            return redirect(f'/guide/#{emergency_type}')
    else:
        form = IncidentReportForm()
    return render(request, 'home.html', {'form': form})


@login_required
def incident_list(request):
    # authorities see all, volunteers see only their assigned ones
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
    return render(request, 'incidents/detail.html', {'incident': incident})


@login_required
def resolve_incident(request, pk):
    if request.user.role != 'authority':
        return redirect('dashboard')
    incident = get_object_or_404(Incident, pk=pk)
    incident.status = 'resolved'
    incident.resolved_at = timezone.now()
    incident.save()
    return redirect('incident_list')


from django.shortcuts import render

# Create your views here.

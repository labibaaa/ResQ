from django.shortcuts import render
from incidents.models import Incident
from incidents.forms import IncidentReportForm
from users.models import User
from evacuation.models import SafeZone
from aid.models import AidStats


def get_home_context(form=None):
    stats = AidStats.objects.first()
    return {
        'active_incidents': Incident.objects.filter(status='active').count(),
        'active_volunteers': User.objects.filter(role='volunteer', is_active=True).count(),
        'safe_zones': SafeZone.objects.filter(is_active=True).count(),
        'lives_saved': stats.lives_saved if stats else 0,
        'form': form or IncidentReportForm(),
    }


def home(request):
    return render(request, 'home.html', get_home_context())
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import SafeZone
from .forms import SafeZoneForm


def evacuation_page(request):
    zones = SafeZone.objects.filter(is_active=True).order_by('zone_type')
    return render(request, 'evacuation/evacuation.html', {'zones': zones})


def safe_zones_json(request):
    zone_type = request.GET.get('type')
    zones = SafeZone.objects.filter(is_active=True)
    if zone_type:
        zones = zones.filter(zone_type=zone_type)
    data = [
        {
            'id': z.id,
            'name': z.name,
            'type': z.get_zone_type_display(),
            'address': z.address,
            'lat': float(z.latitude),
            'lng': float(z.longitude),
            'capacity': z.capacity,
            'availability': z.availability(),
            'is_full': z.is_full(),
            'notes': z.notes,
        }
        for z in zones
    ]
    return JsonResponse({'zones': data})


@login_required
def zone_create(request):
    if request.user.role != 'authority':
        return redirect('evacuation_page')
    if request.method == 'POST':
        form = SafeZoneForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.added_by = request.user
            obj.save()
            return redirect('evacuation_page')
    else:
        form = SafeZoneForm()
    return render(request, 'evacuation/edit.html', {'form': form})


@login_required
def zone_edit(request, pk):
    if request.user.role != 'authority':
        return redirect('evacuation_page')
    zone = get_object_or_404(SafeZone, pk=pk)
    if request.method == 'POST':
        form = SafeZoneForm(request.POST, instance=zone)
        if form.is_valid():
            form.save()
            return redirect('evacuation_page')
    else:
        form = SafeZoneForm(instance=zone)
    return render(request, 'evacuation/edit.html', {'form': form})


@login_required
def update_occupancy(request, pk):
    if request.user.role != 'authority':
        return redirect('evacuation_page')
    zone = get_object_or_404(SafeZone, pk=pk)
    if request.method == 'POST':
        occupancy = request.POST.get('current_occupancy')
        try:
            zone.current_occupancy = int(occupancy)
            zone.save()
        except (ValueError, TypeError):
            pass
    return redirect('evacuation_page')
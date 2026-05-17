from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .forms import CashDonationForm, GoodsDonationForm, AidStatsForm
from .models import CashDonation, GoodsDonation, AidStats
from users.models import User


def get_stats():
    stats_obj = AidStats.objects.first()
    lives_saved = stats_obj.lives_saved if stats_obj else 0
    total_donors = (
        CashDonation.objects.filter(status='verified').count() +
        GoodsDonation.objects.filter(status='received').count()
    )
    total_cash = CashDonation.objects.filter(
        status='verified'
    ).aggregate(total=Sum('amount'))['total'] or 0
    total_goods = GoodsDonation.objects.filter(status='received').count()
    active_volunteers = User.objects.filter(
        role='volunteer', is_active=True
    ).count()
    return {
        'lives_saved': lives_saved,
        'total_donors': total_donors,
        'total_cash': total_cash,
        'total_goods': total_goods,
        'active_volunteers': active_volunteers,
    }


def aid_page(request):
    return render(request, 'aid/aid.html', get_stats())


def donate_cash(request):
    if request.method == 'POST':
        form = CashDonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('aid_page')
    else:
        form = CashDonationForm()
    return render(request, 'aid/donate.html', {'form': form, 'type': 'cash'})


def donate_goods(request):
    if request.method == 'POST':
        form = GoodsDonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('aid_page')
    else:
        form = GoodsDonationForm()
    return render(request, 'aid/donate.html', {'form': form, 'type': 'goods'})


@login_required
def verify_cash_donation(request, pk):
    if request.user.role != 'authority':
        return redirect('dashboard')
    donation = get_object_or_404(CashDonation, pk=pk)
    donation.status = 'verified'
    donation.verified_by = request.user
    donation.save()
    return redirect('donation_list')


@login_required
def mark_goods_received(request, pk):
    if request.user.role != 'authority':
        return redirect('dashboard')
    donation = get_object_or_404(GoodsDonation, pk=pk)
    donation.status = 'received'
    donation.save()
    return redirect('donation_list')


@login_required
def donation_list(request):
    if request.user.role != 'authority':
        return redirect('dashboard')
    cash = CashDonation.objects.all().order_by('-donated_at')
    goods = GoodsDonation.objects.all().order_by('-donated_at')
    return render(request, 'aid/donation_list.html', {
        'cash_donations': cash,
        'goods_donations': goods,
        'total_cash_verified': CashDonation.objects.filter(
            status='verified').aggregate(t=Sum('amount'))['t'] or 0,
        'total_goods_received': GoodsDonation.objects.filter(status='received').count(),
        'pending_cash': CashDonation.objects.filter(status='pending').count(),
    })


@login_required
def update_lives_saved(request):
    if request.user.role != 'authority':
        return redirect('dashboard')
    stats = AidStats.objects.first() or AidStats()
    if request.method == 'POST':
        form = AidStatsForm(request.POST, instance=stats)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.updated_by = request.user
            obj.save()
            return redirect('aid_page')
    else:
        form = AidStatsForm(instance=stats)
    return render(request, 'aid/update_stats.html', {'form': form})
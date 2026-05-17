from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignupForm


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignupForm()
    return render(request, 'users/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']
        user = authenticate(request, username=username, password=password)
        if user and user.role == role:
            if role == 'authority' and not user.is_verified:
                return render(request, 'users/login.html', {
                    'error': 'Your authority account is pending admin verification.'
                })
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid credentials.'})
    return render(request, 'users/login.html')


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def dashboard_view(request):
    return render(request, 'users/dashboard.html', {'user': request.user})
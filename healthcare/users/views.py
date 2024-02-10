# views.py
# views.py

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django_otp.plugins.otp_totp.models import TOTPDevice
from django.contrib.auth.models import User

from .forms import LoginForm


def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Check if user has 2FA enabled
                if TOTPDevice.objects.filter(user=user, confirmed=True).count() > 0:
                    return render(request, '2fa.html', {'user_id': user.id})
                else:
                    login(request, user)
                    return redirect('dashboard')
            else:
                return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html', {'form': form})

def verify_2fa(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        otp_code = request.POST.get('otp_code')

        try:
            user = User.objects.get(pk=user_id)
            totp_device = TOTPDevice.objects.get(user=user, confirmed=True)
            if totp_device.verify_otp(otp_code):
                login(request, user)
                return redirect('dashboard')
            else:
                return render(request, '2fa.html', {'user_id': user_id, 'error': 'Invalid 2FA code'})
        except TOTPDevice.DoesNotExist:
            return render(request, 'login.html', {'error': '2FA not enabled for this user'})

    return redirect('login')


def dashboard(request):
    if request.user.is_authenticated:
        # Redirect to the appropriate dashboard based on user type
        if request.user.is_patient:
            return redirect('patient_dashboard')
        # Add other user types as needed
    return redirect('login')


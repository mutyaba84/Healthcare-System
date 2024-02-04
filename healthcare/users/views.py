# views.py
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django_otp.plugins.otp_totp.models import TOTPDevice
from django.contrib.auth.models import User  # Import User model
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Check if user has 2FA enabled
            if TOTPDevice.objects.filter(user=user, confirmed=True).count() > 0:
                # Implement logic to send 2FA code via email or SMS
                return render(request, '2fa.html', {'user_id': user.id})
            else:
                login(request, user)
                return redirect('dashboard')
        else:
            # Handle invalid login credentials
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')

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
                return render(request, 'verify_2fa.html', {'user_id': user_id, 'error': 'Invalid 2FA code'})
        except TOTPDevice.DoesNotExist:
            return render(request, 'login.html', {'error': '2FA not enabled for this user'})

    return redirect('login')




@login_required
def assign_role(request, role_name):
    user = request.user.customuser
    role = UserRole.objects.get(name=role_name)
    user.role = role
    user.save()
    return redirect('dashboard')


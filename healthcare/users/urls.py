from django.urls import path
from .views import login_view, dashboard, verify_2fa

app_name = 'users'  # Add this line if you want to namespace your URLs

urlpatterns = [
    path('login/', login_view, name='login'),
    path('verify-2fa/', verify_2fa, name='verify_2fa'),
    path('dashboard/', dashboard, name='dashboard'),
    # Add other user-related URLs as needed
    
    
]

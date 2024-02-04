from django.urls import path
from .views import patient_search, patient_details

urlpatterns = [
    path('search/', patient_search, name='patient_search'),
    path('details/<int:patient_id>/', patient_details, name='patient_details'),
]

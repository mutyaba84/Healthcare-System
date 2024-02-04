from django.contrib import admin
from .models import Patient
from .forms import PatientForm

class PatientAdmin(admin.ModelAdmin):
    form = PatientForm
    list_display = ('id', 'first_name', 'last_name', 'date_of_birth', 'contact_details', 'insurance_information')

admin.site.register(Patient, PatientAdmin)

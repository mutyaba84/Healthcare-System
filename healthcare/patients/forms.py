# forms.py
from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'date_of_birth', 'contact_details', 'insurance_information',
                  'pre_existing_conditions', 'allergies', 'surgeries_or_treatments']

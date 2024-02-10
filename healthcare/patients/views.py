# views.py
from django.shortcuts import render, get_object_or_404
from .models import Patient
from django.shortcuts import render


def patient_search(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query', '')
        patients = Patient.objects.filter(
            first_name__icontains=search_query) | Patient.objects.filter(last_name__icontains=search_query)
        return render(request, 'patient_search_results.html', {'patients': patients})
    return render(request, 'patient_search.html')

def patient_details(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    # Implement verification logic here
    return render(request, 'patient_details.html', {'patient': patient})

def dashboard(request):
    return render(request, 'patients/dashboard.html')







from django.db import models


class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    contact_details = models.CharField(max_length=200)
    insurance_information = models.CharField(max_length=200)
    # Medical History Fields
    pre_existing_conditions = models.TextField(blank=True)
    allergies = models.TextField(blank=True)
    surgeries_or_treatments = models.TextField(blank=True)
    # other relevant patient information

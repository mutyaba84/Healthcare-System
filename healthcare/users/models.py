# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add any additional fields you want for your user model
    # For example:
    date_of_birth = models.DateField(null=True, blank=True)
    contact_number = models.CharField(max_length=15, null=True, blank=True)

    # Add any other custom fields or methods as needed

    def __str__(self):
        return self.username

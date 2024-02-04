from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.auth.models import Group

class UserRole(models.Model):
    name = models.CharField(max_length=50, unique=True)

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(UserRole, on_delete=models.SET_NULL, null=True)
    


class Nurse(Group):
    pass

class Physician(Group):
    pass

class AdminStaff(Group):
    pass

nurse_group, created = Nurse.objects.get_or_create(name='Nurse')
physician_group, created = Physician.objects.get_or_create(name='Physician')
admin_group, created = AdminStaff.objects.get_or_create(name='AdminStaff')

# Assign permissions to groups
nurse_group.permissions.add(
    Permission.objects.get(codename='view_patient_information'),
    Permission.objects.get(codename='edit_patient_information'),
    # Add other permissions specific to nurses
)

physician_group.permissions.add(
    Permission.objects.get(codename='view_patient_information'),
    # Add other permissions specific to physicians
)

admin_group.permissions.add(
    Permission.objects.get(codename='manage_users'),
    # Add other admin-related permissions
)


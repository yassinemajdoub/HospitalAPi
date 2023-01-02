from pickle import TRUE

from django.contrib.auth import get_user_model
from django.db import models
from Provider.models import Provider
# Create your models here.

class Patient(models.Model):
    full_name = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20 ,unique=True)
    email = models.EmailField()
    emergency_contact_phone = models.CharField(max_length=20, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True )
    
    def __str__(self) -> str:
        return f"{self.full_name}-{self.email}"

    class Meta:
        ordering = ["-created"]
    

class LabResult(models.Model):
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE)
    test_name = models.CharField(max_length=100)
    test_result = models.JSONField()
    test_date = models.DateField()

class Appointment(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    provider = models.ForeignKey('Provider.Provider', on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    location = models.CharField(max_length=255 ,blank=True)
    reason = models.TextField(blank=True)
    notes = models.TextField(blank=True)



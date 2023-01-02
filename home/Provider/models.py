from django.db import models

class Provider(models.Model):
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
from django.db import models

# Create your models here.

class Resource(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    availability = models.BooleanField()

    def save(self, *args, **kwargs):
        self.availability = Resource.objects.filter(type=self.type).exists()
        super().save(*args, **kwargs)
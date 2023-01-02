from django.db import models
import datetime

class trackingModel(models.Model):
    default_value = datetime.datetime.now()
    create_at=models.DateTimeField(auto_now_add=True )
    updated_at=models.DateTimeField(auto_now=True )

    class Meta:
       abstract=True
       
from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Details(models.Model):
    firstname =CharField(max_length=100, blank=True, null=True)
    lastname =CharField(max_length=100, blank=True, null=True)
    identification_number = models.CharField(max_length=100, blank=True, null=True)
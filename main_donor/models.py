from django.db import models


# Create your models here.

class RegistrationDonor(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=100)

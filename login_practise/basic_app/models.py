from django.db import models

# Create your models here.

class TeamProfile(models.Model):
    username = models.CharField(max_length=500)
    captain = models.CharField(max_length = 500)
    manager = models.CharField(max_length = 500)
    contact_number = models.IntegerField()
    COUNTRIES = (('INDIA','INDIA'),('GERMANY','GERMANY'),('SPAIN','SPAIN'),('RUSSIA','RUSSIA'),('FRANCE','FRANCE'),('ENGLAND','ENGLAND'))
    country = models.CharField(max_length = 500,choices = COUNTRIES)

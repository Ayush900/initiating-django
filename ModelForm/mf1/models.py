from django.db import models
from ModelForm import settings

# Create your models here.
class StudentDetails(models.Model):

    name = models.CharField(max_length = 300)
    branch = models.CharField(max_length = 300)
    phone_no = models.IntegerField(unique = True)
    email_id = models.EmailField()
    Date_of_birth = models.DateField()

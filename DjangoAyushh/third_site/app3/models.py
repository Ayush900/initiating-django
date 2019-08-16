from django.db import models

# Create your models here.

class Topic(models.Model):
    top_name = models.CharField(max_length=264,unique=True)

    def __str__(self):
        return str(self.top_name)

class Web_page(models.Model):

    topic = models.ForeignKey(Topic,on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return str(self.name)

class Acess_record(models.Model):

    name = models.ForeignKey(Web_page,on_delete=models.DO_NOTHING)
    date = models.DateField()

    def __str__(self):
        return str(self.date)
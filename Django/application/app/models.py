from django.db import models

# Create your models here.
class person(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    pH = models.IntegerField(null = True)
from django.db import models

# Create your models here.


class Registration(models.Model):
    name = models.CharField()
    email = models.EmailField()
    number = models.IntegerField()
    year = models.IntegerField()

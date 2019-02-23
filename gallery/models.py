from django.db import models

# Create your models here.


class Gallery(models.Model):
    Image = models.ImageField(upload_to="gallery/")
    Event_name = models.CharField(max_length=500)


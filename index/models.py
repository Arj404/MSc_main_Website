from django.db import models

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=50)
    USER_TYPE_CHOICES = (('1st', 'GENERAL SECRETARY'), ('2nd', 'FINANCIAL SECRETARY'), ('3rd', 'JOINT SECRETARY'))
    post = models.CharField(max_length=50, choices=USER_TYPE_CHOICES, default='3rd')
    Image = models.ImageField(upload_to="team/")
    fb_link = models.URLField(max_length=50, null=True, blank=True)
    git_link = models.URLField(max_length=50, null=True, blank=True)
    linked_in_link = models.URLField(max_length=50, null=True, blank=True)


class Events(models.Model):
    heading = models.CharField(max_length=50)
    Image = models.ImageField(upload_to="events/")
    description = models.CharField(max_length=500)


class Gallery(models.Model):
    Image = models.ImageField(upload_to="gallery/")


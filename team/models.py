from django.db import models

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=50)
    Image = models.ImageField(upload_to="team/")
    fb_link = models.URLField(max_length=50, null=True, blank=True)
    git_link = models.URLField(max_length=50, null=True, blank=True)
    linked_in_link = models.URLField(max_length=50, null=True, blank=True)
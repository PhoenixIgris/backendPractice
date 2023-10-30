from django.db import models

# Create your models here.
class MyProjectsModel(models.Model):
    name = models.CharField(max_length = 255)
    detail  = models.CharField(max_length = 255)
    url = models.CharField(max_length = 255)
    image = models.CharField(max_length = 255)
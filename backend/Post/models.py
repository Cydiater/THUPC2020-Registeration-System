from django.db import models

# Create your models here.

class post(models.Model):
    content = models.TextField()
    title = models.TextField()
    author = models.CharField(max_length=20)
    timestamp = models.IntegerField()
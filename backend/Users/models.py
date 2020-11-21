from django.db import models

# Create your models here.


class user(models.Model):
    teamname = models.CharField(max_length=20)
    password = models.CharField(max_length=16, null=False, blank=False)
    type = models.CharField(max_length=1, default='')
    isAdmin = models.BooleanField(default=False)


class member(models.Model):
    school = models.CharField(max_length=20)
    name = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    email = models.CharField(max_length=30, default='')
    location = models.CharField(max_length=30, default='')
    phone = models.CharField(max_length=30, default='')


class user2member(models.Model):
    userid = models.IntegerField()
    memberid = models.IntegerField()

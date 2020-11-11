from django.db import models

# Create your models here.


class user(models.Model):
    teamname = models.CharField(max_length=20)
    password = models.CharField(max_length=16, null=False, blank=False)
    email = models.CharField(max_length=30, default='')
    type = models.CharField(max_length=1, default='')
    isAdmin = models.BooleanField(default=False)


class member(models.Model):
    name = models.CharField(max_length=10)
    school = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)


class user2member(models.Model):
    userid = models.IntegerField()
    memberid = models.IntegerField()


class post(models.Model):
    content = models.TextField()
    title = models.TextField()
    author = models.CharField(max_length=20)
    timestamp = models.IntegerField()
    post_id = models.IntegerField()

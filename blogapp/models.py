from django.db import models


class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    password = models.CharField(max_length=32, null=True, blank=True)


class Post(models.Model):
    pass
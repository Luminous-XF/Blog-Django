from django.db import models


class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    password = models.CharField(max_length=32, null=True, blank=True)


class Post(models.Model):
    uuid = models.CharField(max_length=36)
    user_id = models.CharField(max_length=36)
    title = models.CharField(max_length=256)
    content = models.TextField()
    STATUS_CHOICE = [
        ('COMMON', 'common'),
        ('TOP', 'top'),
        ('ESSENCE', 'essence'),
    ]
    type = models.CharField(max_length=10, choices=STATUS_CHOICE,default='COMMON')
    comment_count = models.BigIntegerField(default=0)
    score = models.FloatField(default=0.0)
    STATUS_CHOICE = [
        ('NORMAL', 'normal'),
        ('AUDIT', 'audit'),
        ('BANNED', 'banned'),
    ]
    status = models.CharField(max_length=10 , choices=STATUS_CHOICE,default='AUDIT')
    likes = models.BigIntegerField(default=0)
    page_views = models.BigIntegerField(default=0)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    STATUS_CHOICE = [
        ('NORMAL', 'normal'),
        ('DELETE', 'delete'),
    ]
    row_status = models.CharField(max_length=10,choices=STATUS_CHOICE,default='NORMAL')

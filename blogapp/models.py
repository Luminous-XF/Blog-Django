from django.db import models


class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    password = models.CharField(max_length=32, null=True, blank=True)

class PostTypeChoice(models.TextChoices):
    COMMON = 'COMMON', 'Common'
    TOP = 'TOP', 'Top'
    ESSENCE = 'ESSENCE', 'Essence'

class PoststatusChoice(models.TextChoices):
    NORMAL = 'NORMAL', 'Normal'
    AUDIT = 'AUDIT', 'Audit'
    BANNED = 'BANNED', 'Banned'

class PostRow_StatusChoice(models.TextChoices):
    NORMAL = 'NORMAL', 'Normal'
    DELETE = 'DELETE', 'Delete'

class Post(models.Model):
    uuid = models.CharField(max_length=36)
    user_id = models.CharField(max_length=36)
    title = models.CharField(max_length=256)
    content = models.TextField()
    type = models.CharField(
        max_length=64,
        choices=PostTypeChoice.choices,
        default=PostTypeChoice.COMMON)
    comment_count = models.BigIntegerField(default=0)
    score = models.FloatField(default=0.0)
    status = models.CharField(
        max_length=64,
        choices=PoststatusChoice.choices,
        default=PoststatusChoice.AUDIT
    )
    likes = models.BigIntegerField(default=0)
    page_views = models.BigIntegerField(default=0)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    row_status = models.CharField(
        max_length=64,
        choices=PostRow_StatusChoice.choices,
        default=PostRow_StatusChoice.NORMAL
    )


class UserUser_TypeChoice(models.TextChoices):
    ADMIN = 'ADMIN', 'Admin'
    COMMON = 'COMMON', 'Common'

class UserUser_StatusChoice(models.TextChoices):
    COMMON = 'COMMON', 'Common'
    BANNED = 'BANNED', 'Banned'
    INACTIVATION = 'INACTIVATION', 'Inactivation'

class UserGenderChoice(models.TextChoices):
    MALE ='MALE', 'Male'
    FEMALE ='FEMALE', 'Female'
    UNKNOWN = 'UNKNOWN', 'Unknown'

class User(models.Model):
    uuid = models.CharField(max_length=36)
    username = models.CharField(max_length=32)
    nickname = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    salt = models.CharField(max_length=16)
    email = models.CharField(max_length=32)
    user_type = models.CharField(
        max_length=64,
        choices=UserUser_TypeChoice.choices,
        default=UserUser_TypeChoice.COMMON)
    user_satus = models.CharField(
        max_length=64,
        choices=UserUser_StatusChoice.choices,
        default=UserUser_StatusChoice.INACTIVATION)
    activation_code = models.CharField(max_length=32)
    header_url = models.CharField(max_length=256)
    create_time = models.DateTimeField()
    gender = models.CharField(
        max_length=64,
        choices=UserGenderChoice.choices,
                default=UserGenderChoice.UNKNOWN)
    brief = models.TextField()
    likes = models.BigIntegerField(default=0)
    page_views = models.BigIntegerField(default=0)


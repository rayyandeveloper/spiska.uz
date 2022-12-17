from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField

class Phone(models.Model):
    number = models.CharField(max_length=20)

    def __str__(self):
        return self.number

#  models.ManyToManyField(Phone)

class User(AbstractUser):
    img = models.ImageField(upload_to='profile-img/', default='default_user.png')
    phone = models.CharField(max_length=20)
    diamond = models.IntegerField(default=0)
    seria_number = models.CharField(null=True, blank=True, max_length=200)
    passport_image = models.ImageField(null=True, blank=True)
    passport_info = models.CharField(max_length=500)


from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.

class CustomUser(AbstractUser):
    mobile_no = models.CharField(max_length = 11, blank = True)
    email_verified = models.BooleanField(default = False)
    verf_link = models.CharField(max_length = 100)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    object = UserManager()



class profile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def _str__(self) -> str: 
        return self.user


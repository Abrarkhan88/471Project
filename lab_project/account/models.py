from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from .manager import UserManager

class CustomUser(AbstractUser):
    mobile_no = models.CharField(max_length = 11, blank = True)
    email_verified = models.BooleanField(default = False)
    verf_link = models.CharField(max_length = 100)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    object = UserManager()

    # Override the groups field with a unique related_name
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Change this to something unique
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )

    # Override the user_permissions field with a unique related_name
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions_set',  # Change this to something unique
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

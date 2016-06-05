from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager

# Create your models here.


class User(AbstractBaseUser):
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def __str__(self):
        return self.username




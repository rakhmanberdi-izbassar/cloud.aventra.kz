from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    role = models.CharField(max_length=20, default='user')  # user/admin/organizer т.б.
    remember_token = models.CharField(max_length=100, blank=True, null=True)

    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

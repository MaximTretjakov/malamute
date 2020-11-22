from django.db import models
from django.contrib.auth.models import AbstractUser


class CiUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)

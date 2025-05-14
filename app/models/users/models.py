from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class ProfileInfo(models.Model):
    user = models.OneToOneField(CustomUser, null=True, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=32, null=True)
    last_name= models.CharField(max_length=32, null=True)
    
    institution_name = models.CharField(max_length=100,null=True)

    num_of_sub =  models.IntegerField(default=0)

    def __str__(self):
        return str(self.user.email)

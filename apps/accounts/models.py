from django.db import models, IntegrityError
from django.contrib.auth.models import AbstractUser

from apps.core.models import Model


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=60, blank=True)
    last_name = models.CharField(max_length=60, blank=True)
    address = models.TextField(blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @classmethod
    def create_user(cls, email, password, **kwargs):
        try:
            user = cls(email=email, **kwargs)
            user.set_password(password)
            user.save()
            return user
        except IntegrityError as error:
            return error

    @classmethod
    def create_superuser(cls, email, password, **kwargs):
        try:
            kwargs.setdefault('is_staff', True)
            kwargs.setdefault('is_superuser', True)
            return cls.create_user(email, password, **kwargs)
        except IntegrityError as error:
            return error


class Role(Model):
    name = models.CharField(max_length=255)
    actions = models.ManyToManyField('Action', related_name='roles')


class Action(Model):
    name = models.CharField(max_length=255)


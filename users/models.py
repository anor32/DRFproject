from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _



NULLABLE = {'blank':True, 'null':True}

class UserRoles(models.TextChoices):
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')


class User(AbstractUser):

    username = models.CharField(max_length=150, unique=False, default=None, verbose_name="username", **NULLABLE)
    email = models.EmailField(unique=True, verbose_name=_('email address'))
    role = models.CharField(max_length=9, choices=UserRoles.choices, default=UserRoles.MEMBER)
    first_name = models.CharField(max_length=50, verbose_name=_('first name'), **NULLABLE)
    last_name = models.CharField(max_length=50, verbose_name=_('last name'), **NULLABLE)
    phone = models.CharField(max_length=20, verbose_name=_('phone number'), **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name=_('is active'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []



    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ['id']


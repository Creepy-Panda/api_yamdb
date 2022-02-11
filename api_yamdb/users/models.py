from django.contrib.auth.models import AbstractUser
from django.db import models


class UserRole:
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'


class CustomUser(AbstractUser):
    """Custom user model."""

    ROLES = [
        (UserRole.USER, 'user'),
        (UserRole.MODERATOR, 'moderator'),
        (UserRole.ADMIN, 'admin'),
    ]

    role = models.CharField(
        choices=ROLES,
        max_length=50,
        verbose_name='Роль пользователя',
        default='user',
    )
    username = models.CharField(
        max_length=150,
        unique=True
    )
    first_name = models.CharField(
        max_length=150,
        blank=True
    )
    last_name = models.CharField(
        max_length=150,
        blank=True
    )
    email = models.EmailField(
        verbose_name='Email',
        max_length=254,
        help_text='Введите адрес электронной почты',
        unique=True
    )
    bio = models.TextField(
        verbose_name='О себе',
        help_text='Напиши что-нибудь о себе',
        null=True
    )

    @property
    def is_admin(self):
        return self.role == UserRole.ADMIN

    @property
    def is_moderator(self):
        return self.role == UserRole.MODERATOR

    class Meta:
        ordering = ['id']

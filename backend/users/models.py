from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from .validators import validate_username


class CustomUser(AbstractUser):
    email = models.EmailField(
        verbose_name='Электронная почта',
        max_length=settings.CUSTOM_USER_EMAIL_MAX_LENGTH,
        unique=True
    )
    username = models.CharField(
        verbose_name='Логин',
        max_length=settings.CUSTOM_USER_USERNAME_MAX_LENGTH,
        unique=True,
        validators=(validate_username,)
    )
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=settings.CUSTOM_USER_FIRST_NAME_MAX_LENGTH
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=settings.CUSTOM_USER_LAST_NAME_MAX_LENGTH
    )
    password = models.CharField(
        verbose_name='Пароль',
        max_length=settings.CUSTOM_USER_PASSWORD_MAX_LENGTH
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', 'first_name', 'last_name')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('last_name', 'first_name')

    def __str__(self):
        return self.username


class Follow(models.Model):
    author = models.ForeignKey(
        CustomUser,
        related_name='follow',
        on_delete=models.CASCADE,
        verbose_name='Автор рецепта'
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик'
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        unique_together = ('user', 'author')
        constraints = (
            models.CheckConstraint(
                check=~models.Q(user=models.F('author')),
                name='no_self_follow'
            ),
        )

    def __str__(self):
        return f'{self.user} {self.author}'

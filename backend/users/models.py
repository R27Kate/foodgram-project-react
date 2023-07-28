from django.contrib.auth.models import AbstractUser
from django.db import models

from .validators import validate_username


class CustomUser(AbstractUser):
    email = models.EmailField(
        verbose_name='Электронная почта',
        max_length=254,
        unique=True
    )
    username = models.CharField(
        verbose_name='Логин',
        max_length=150,
        unique=True,
        validators=(validate_username,)
    )
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=150
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=150
    )
    password = models.CharField(
        verbose_name='Пароль',
        max_length=150
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', 'first_name', 'last_name')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('id',)

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
        ordering = ('-pk',)
        unique_together = ('user', 'author')
        constraints = (
            models.CheckConstraint(
                check=~models.Q(user=models.F('author')),
                name='no_self_follow'
            ),
        )

    def __str__(self):
        return f'{self.user} {self.author}'

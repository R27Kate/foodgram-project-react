from django.contrib.auth import get_user_model
from django.db.models import Prefetch

from foodgram.common.common_services import (
    create_model_instance,
    delete_model_instance)
from recipes.models import Recipe
from users.models import Follow

User = get_user_model()


def get_authors_user_is_following_with_recipes(user):
    '''получаем авторов из подписок с их рецептами'''
    recipes = Prefetch('recipes', Recipe.objects.all())
    return User.objects.prefetch_related(recipes).filter(follow__user=user)


def add_author_follow(author, user):
    '''метод подписки на автора'''
    return create_model_instance(Follow, author=author, user=user)


def delete_author_follow(author, user):
    '''метод удаления подписки на автора'''
    return delete_model_instance(Follow, author=author, user=user)

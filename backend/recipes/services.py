from django.db.models import Prefetch

from foodgram.common.common_services import (create_model_instance,
                                             delete_model_instance)
from recipes.models import (IngredientInRecipe,
                            Recipe,
                            Favourite,
                            ShoppingCart)
from users.models import Follow


def get_recipes_for_serialization(user_id):
    '''Функция для получения сериализованных объектов рецептов,
       связанных с пользователем c id.'''
    favourites = Prefetch(
        'favourites',
        Favourite.objects.filter(user_id=user_id))

    shopping_recipe = Prefetch(
        'shopping_recipe',
        ShoppingCart.objects.filter(user_id=user_id))

    ingredient_list = Prefetch(
        'ingredient_list',
        IngredientInRecipe.objects.select_related('ingredient')
    )
    author_followers = Prefetch(
        'author__follow',
        Follow.objects.filter(user_id=user_id))

    return Recipe.objects \
        .select_related('author') \
        .prefetch_related(favourites, shopping_recipe,
                          ingredient_list, author_followers,
                          'tags').all()


def add_recipe_to_shopping_cart(recipe, user):
    '''Функция для добавлениия рецепта в список покупок
       для указанного пользователя.'''
    return create_model_instance(ShoppingCart, recipe=recipe, user=user)


def delete_recipe_from_shopping_cart(recipe, user):
    '''Функция для удаления рецепта из списока покупок
       для указанного пользователя.'''
    return delete_model_instance(ShoppingCart, recipe=recipe, user=user)


def get_recipes_from_shopping_cart(user):
    '''Функция для получения рецептов из списка покупок
       для указанного пользователя.'''
    return Recipe.objects\
        .prefetch_related('ingredient_list')\
        .filter(shopping_recipe__user=user)


def add_recipe_to_favourite(recipe, user):
    '''Функция для добавлениия рецепта в избранное
       для указанного пользователя.'''
    return create_model_instance(Favourite, recipe=recipe, user=user)


def delete_recipe_from_favourite(recipe, user):
    '''Функция для удаления рецепта из избранного
       для указанного пользователя.'''
    return delete_model_instance(Favourite, recipe=recipe, user=user)

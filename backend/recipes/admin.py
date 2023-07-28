from django.contrib.admin import ModelAdmin, register

from .models import (
    Ingredient, IngredientInRecipe, Recipe,
    Tag, TagInRecipe, Favourite, ShoppingCart
)


@register(Ingredient)
class IngredientAdmin(ModelAdmin):
    list_display = ('pk', 'name', 'unit_of_measurement')
    list_filter = ('name',)
    search_fields = ('name',)


@register(Tag)
class TagAdmin(ModelAdmin):
    list_display = ('pk', 'name', 'color', 'slug')


@register(Recipe)
class RecipeAdmin(ModelAdmin):
    list_display = ('pk', 'name', 'author', 'get_favourites',
                    'get_tags', 'created')
    list_filter = ('author', 'name', 'tags')
    search_fields = ('name',)

    def get_favourites(self, obj):
        return obj.favourites.count()

    get_favourites.short_description = 'Рецепт добавлен в избранное'

    def get_tags(self, obj):
        return '\n'.join(obj.tags.values_list('name', flat=True))

    get_tags.short_description = 'Тэг или список тэгов'


@register(IngredientInRecipe)
class IngredientInRecipe(ModelAdmin):
    list_display = ('pk', 'recipe', 'ingredient', 'amount')


@register(TagInRecipe)
class TagAdmin(ModelAdmin):
    list_display = ('pk', 'tag', 'recipe')


@register(Favourite)
class FavoriteAdmin(ModelAdmin):
    list_display = ('pk', 'user', 'recipe')


@register(ShoppingCart)
class ShoppingCartAdmin(ModelAdmin):
    list_display = ('pk', 'user', 'recipe')

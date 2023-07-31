from drf_extra_fields import fields
from rest_framework import serializers

from recipes.models import Ingredient, Tag, IngredientInRecipe, Recipe
from users.serializers import CustomUserSerializer
from recipes.validators import (
    validate_ingredients,
    validate_tags,
    validate_cooking_time)


class IngredientSerializer(serializers.ModelSerializer):
    '''Сериализатор для модели Ingredient.'''
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'unit_of_measurement')


class TagSerializer(serializers.ModelSerializer):
    '''Сериализатор для модели Tag.'''
    class Meta:
        model = Tag
        fields = ('id', 'name', 'color', 'slug')


class IngredientInRecipeSerializer(serializers.ModelSerializer):
    '''Сериализатор для модели IngredientInRecipe.'''
    id = serializers.ReadOnlyField(source='ingredient.id')
    name = serializers.ReadOnlyField(source='ingredient.name')
    unit_of_measurement = serializers.ReadOnlyField(
        source='ingredient.unit_of_measurement')

    class Meta:
        model = IngredientInRecipe
        fields = ('id', 'name', 'unit_of_measurement', 'amount')


class RecipeSerializer(serializers.ModelSerializer):
    '''Сериализатор для модели Recipe c добавлением
       в избранное и в список покупок'''
    tags = TagSerializer(many=True)
    author = CustomUserSerializer()
    ingredients = IngredientInRecipeSerializer(
        source='ingredient_list',
        many=True
    )
    is_favorited = serializers.SerializerMethodField()
    is_in_shopping_cart = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = ('id', 'tags', 'author', 'ingredients',
                  'image', 'name', 'text', 'cooking_time',
                  'is_favorited', 'is_in_shopping_cart',)

    @staticmethod
    def get_is_favorited(recipe):
        '''проверка на добавление рецепта в избранное'''
        return recipe.favourites.exists()

    @staticmethod
    def get_is_in_shopping_cart(recipe):
        '''проверка на добавление рецепта в список покупок'''
        return recipe.shopping_recipe.exists()


class CreateIngredientInRecipeSerializer(serializers.ModelSerializer):
    '''Сериализатор для добавления ингредиентов в рецепт.'''
    id = serializers.PrimaryKeyRelatedField(
        source='ingredient',
        queryset=Ingredient.objects.all())

    class Meta:
        model = IngredientInRecipe
        fields = ('id', 'amount')


class SaveRecipeSerializer(serializers.ModelSerializer):
    '''Сериализатор для создания и обновления рецепта.'''
    tags = serializers.PrimaryKeyRelatedField(many=True,
                                              queryset=Tag.objects.all())
    ingredients = CreateIngredientInRecipeSerializer(many=True)
    image = fields.Base64ImageField()
    cooking_time = serializers.IntegerField(min_value=1)

    class Meta:
        model = Recipe
        fields = ('ingredients', 'tags', 'name',
                  'image', 'text', 'cooking_time')

    def validate(self, data):
        validate_tags(self.initial_data.get('tags')),
        validate_ingredients(
            self.initial_data.get('ingredients')
        )
        validate_cooking_time(
            self.initial_data.get('cooking_time')
        )
        return data

    def create(self, validated_data):
        '''создание нового рецепта со связанными
           ингредиентами и тэгами'''
        ingredients_data = validated_data.pop('ingredients')
        tags_data = validated_data.pop('tags')

        recipe = Recipe.objects.create(**validated_data)
        self._link_ingredients_to_recipe(recipe, ingredients_data)

        recipe.tags.set(tags_data)

        return recipe

    def update(self, recipe, validated_data):
        '''изменение рецепта и связанных ингредиентов и тэгов'''
        ingredients_data = validated_data.pop('ingredients', None)
        tags_data = validated_data.pop('tags', None)

        for attr, value in validated_data.items():
            setattr(recipe, attr, value)

        if ingredients_data is not None:
            IngredientInRecipe.objects.filter(recipe=recipe).delete()
            self._link_ingredients_to_recipe(recipe, ingredients_data)

        if tags_data is not None:
            recipe.tags.set(tags_data)

        instance = super().update(recipe, validated_data)
        return instance

    @staticmethod
    def _link_ingredients_to_recipe(recipe, ingredients_data):
        '''метод для связи ингредиентов с рецептами'''

        ingredient_relations = []
        for ingredient_data in ingredients_data:
            ingredient = ingredient_data['ingredient']
            amount = ingredient_data['amount']
            ingredient_relations.append(
                IngredientInRecipe(recipe=recipe, ingredient=ingredient, amount=amount)
            )
        IngredientInRecipe.objects.bulk_create(ingredient_relations)


class RecipePreviewSerializer(serializers.ModelSerializer):
    '''Сериализатор для превью рецепта.'''
    class Meta:
        model = Recipe
        fields = ('id', 'name', 'image', 'cooking_time')

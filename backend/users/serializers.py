from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers

from users.models import CustomUser


class CustomUserSerializer(UserSerializer):
    '''Сериализатор для CustomUser'''
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ('email', 'id', 'username',
                  'first_name', 'last_name',
                  'is_subscribed')

    @staticmethod
    def get_is_subscribed(serializable_user):
        '''проверка подписки'''
        return serializable_user.follow.exists()


class CustomUserSerializerWithRecipes(CustomUserSerializer):
    '''Сериализатор для пользователя с информацией о его рецептах.'''
    recipes = serializers.SerializerMethodField()
    recipes_count = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ('email', 'id', 'username', 'first_name',
                  'last_name', 'is_subscribed', 'recipes', 'recipes_count')

    def get_recipes(self, user):
        '''получаем рецепты пользователя'''
        from recipes.serializers import RecipePreviewSerializer

        recipes_limit_param_name = self.context['view']\
            .recipes_limit_param_name
        limit = self.context['request'].query_params\
            .get(recipes_limit_param_name)
        return RecipePreviewSerializer(user.recipes.all()[:limit],
                                       many=True).data

    def get_recipes_count(self, user):
        '''получаем количество рецептов пользователя'''
        recipes_limit_param_name = self.context['view']\
            .recipes_limit_param_name
        limit = self.context['request'].query_params.get(
            recipes_limit_param_name,
            float('inf'))
        return min(user.recipes.count(), limit)


class CustomCreateUserSerializer(UserCreateSerializer):
    '''Сериализатор для создания пользователя'''
    class Meta:
        model = CustomUser
        fields = ('email', 'id', 'username',
                  'first_name', 'last_name',
                  'password')
        extra_kwargs = {'password': {'write_only': True}}

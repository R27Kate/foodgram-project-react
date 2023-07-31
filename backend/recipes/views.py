from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from foodgram.common.common_mixins import\
    CreateAndDeleteObjectWithCurrentUserMixin
from foodgram.common.common_permissions import (
    IsAuthenticatedOrRaise401,
    IsAuthenticatedOrReadOnlyOrRaise401)
from recipes import errors
from recipes.filters import IngredientSearchFilter, RecipeFilter
from recipes.models import Ingredient, Tag, Recipe
from recipes.paginators import PageNumberLimitPagination
from recipes.permissions import RecipePermission
from recipes.serializers import (IngredientSerializer, TagSerializer,
                                 RecipeSerializer, SaveRecipeSerializer,
                                 RecipePreviewSerializer)
from recipes.services import (get_recipes_for_serialization,
                              add_recipe_to_shopping_cart,
                              delete_recipe_from_shopping_cart,
                              get_recipes_from_shopping_cart,
                              add_recipe_to_favourite,
                              delete_recipe_from_favourite)
from recipes.utils import RecipeTXTCreator


class TagViewSet(ReadOnlyModelViewSet):
    '''Вьюсет для просмотра тэгов'''
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class IngredientViewSet(ReadOnlyModelViewSet):
    '''Вьюсет для просмотра ингредиентов'''
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    filter_backends = (IngredientSearchFilter,)
    search_fields = ('^name',)


class RecipeViewSet(CreateAndDeleteObjectWithCurrentUserMixin,
                    ModelViewSet):
    '''Вьюсет для создания, изменения, просмотра и удаления рецептов'''
    http_method_names = ['get', 'post', 'patch', 'delete']
    queryset = Recipe.objects.select_related('author', 'favourites')
    permission_classes = (IsAuthenticatedOrReadOnlyOrRaise401,
                          RecipePermission)
    pagination_class = PageNumberLimitPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RecipeFilter

    serializer_class_for_objs_with_user = RecipePreviewSerializer

    def create(self, request, *args, **kwargs):
        '''создаем новый рецепт и получаем ответ с данными рецепта'''
        return Response(self._save(), status.HTTP_201_CREATED)

    def partial_update(self, request, *args, **kwargs):
        '''частично обновляем рецепт и получаем
           ответ с обновленным рецептом'''
        recipe = self.get_object()
        return Response(self._save(recipe), status.HTTP_200_OK)

    @action(detail=False, permission_classes=(IsAuthenticatedOrRaise401,))
    def download_shopping_cart(self, reqeust):
        '''загружаем список покупок'''
        recipes = get_recipes_from_shopping_cart(reqeust.user)
        file = RecipeTXTCreator(recipes).create()
        response = HttpResponse(file, content_type='text/plain')
        response['Content-Disposition'] = \
            f'attachment; filename={RecipeTXTCreator.file_name}'
        return response

    @action(detail=True, methods=('POST', 'DELETE'), url_path='shopping_cart',
            permission_classes=(IsAuthenticatedOrRaise401,))
    def process_shopping_cart(self, request, pk=None):
        '''добавляем и удаляем рецепт из списка покупок'''
        if request.method == 'POST':
            return self.create_with_user(
                add_recipe_to_shopping_cart,
                errors.RECIPE_IS_ALREADY_ON_SHOPPING_CART)
        return self.delete_with_user(
            delete_recipe_from_shopping_cart,
            errors.RECIPE_IS_NOT_ON_SHOPPING_CART)

    @action(detail=True, methods=('POST', 'DELETE'), url_path='favorite',
            permission_classes=(IsAuthenticatedOrRaise401,))
    def process_favorite(self, request, pk=None):
        '''добавляем и удаляем рецепт в избранном'''
        if request.method == 'POST':
            return self.create_with_user(add_recipe_to_favourite,
                                         errors.RECIPE_IS_ALREADY_IN_FAVORITE)
        return self.delete_with_user(delete_recipe_from_favourite,
                                     errors.RECIPE_IS_NOT_IN_FAVORITE)

    def _save(self, instance=None):
        '''вспомогательный метод для сохранения рецепта'''
        serializer_to_save = self.get_serializer(instance, self.request.data)
        serializer_to_save.is_valid(raise_exception=True)
        created_recipe = serializer_to_save.save(author=self.request.user)
        recipe_to_return = get_recipes_for_serialization(self.request.user.id)\
            .get(id=created_recipe.id)
        serializer_to_return = RecipeSerializer(recipe_to_return)
        return serializer_to_return.data

    def get_queryset(self):
        '''метод для получения объектов для выполнения запросов к БД'''
        if self.action not in ('retreive', 'list'):
            return Recipe.objects.all()

        user_id = (
            self.request.user.id
            if self.request.user.is_authenticated
            else 0
        )
        return get_recipes_for_serialization(user_id)

    def get_serializer_class(self):
        '''метод для сериализации и десериализации объектов'''
        if self.request.method in ('POST', 'PATCH'):
            return SaveRecipeSerializer

        return RecipeSerializer

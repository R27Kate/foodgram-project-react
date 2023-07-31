from django_filters import ModelMultipleChoiceFilter
from django_filters import FilterSet, NumberFilter
from rest_framework.filters import SearchFilter

from recipes.models import Recipe, Tag
from recipes.validators import check_int_is_bool


class IngredientSearchFilter(SearchFilter):
    '''Фильтр для поиска ингредиентов по названию'''
    search_param = 'name'


class RecipeFilter(FilterSet):
    '''Фильтры для избранного, списка покупок и тэгов
       по индетификатору пользователя '''
    is_favorited = NumberFilter(method='get_is_favorited',
                                validators=(check_int_is_bool,))
    is_in_shopping_cart = NumberFilter(method='get_is_in_shopping_cart',
                                       validators=(check_int_is_bool,))
    tags = ModelMultipleChoiceFilter(
        field_name='tags__slug',
        to_field_name='slug',
        queryset=Tag.objects.all(),
    )

    class Meta:
        model = Recipe
        fields = ('tags', 'author', 'is_favorited', 'is_in_shopping_cart')

    def get_is_favorited(self, queryset, name, value):
        '''получение отфильтрованного списка рецептов из избранного'''
        return self._filter_by_bool_condition_with_user(
            queryset, name, value, 'favourites__user_id')

    def get_is_in_shopping_cart(self, queryset, name, value):
        '''получение отфильтрованного списка рецептов из списка покупок'''
        return self._filter_by_bool_condition_with_user(
            queryset, name, value, 'shopping_recipe__user')

    def _filter_by_bool_condition_with_user(self,
                                            queryset,
                                            name,
                                            value,
                                            user_condition):
        '''приватный метод для фильтрации по булевому значению
           с учетом пользователя'''
        #user = self.request.user
        user_id = self.request.user.id if self.request.user.is_authenticated else 0
        method = 'filter' if value else 'exclude'
        return getattr(queryset, method)(**{user_condition: user_id})

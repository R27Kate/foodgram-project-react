from django_filters import filters, FilterSet

from users.validators import check_int_is_positive


class RecipesLimitFilter(FilterSet):
    '''Фильтр для ограничения количества рецептов '''
    recipes_limit = filters.NumberFilter(
        method='process_recipes_limit',
        validators=(check_int_is_positive,)
    )

    def process_recipes_limit(self, queryset, name, value):
        self.request.query_params._mutable = True
        self.request.query_params[name] = int(value)
        return queryset

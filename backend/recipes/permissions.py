from rest_framework.permissions import BasePermission


class RecipePermission(BasePermission):
    '''Определение прав доступа к объекту рецепта'''

    def has_object_permission(self, request, view, recipe):
        if request.method in ('PATCH', 'DELETE'):
            return request.user == recipe.author

        return True

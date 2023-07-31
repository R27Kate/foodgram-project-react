from rest_framework.permissions import BasePermission


class RecipePermission(BasePermission):
    '''Определение прав доступа к объекту рецепта'''
    def has_object_permission(self, request, view, recipe):
        return (
            request.user == recipe.author
            if request.method in ('PATCH', 'DELETE')
            else True
        )

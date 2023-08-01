from rest_framework.permissions import (
    BasePermission,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly
)


class ProfilePermission(BasePermission):
    '''Класс для определения прав доступа
       к профилю пользователя'''
    def has_permission(self, request, view):
        if view.action in ('me', 'set_password'):
            return IsAuthenticated().has_permission(
                request,
                view)

        return IsAuthenticatedOrReadOnly().has_permission(
            request,
            view)

from rest_framework.exceptions import NotAuthenticated
from rest_framework.permissions import (BasePermission,
                                        IsAuthenticatedOrReadOnly)


class IsAuthenticatedOrRaise401(BasePermission):
    '''Пермишен с проверкой аутентификации пользователя'''

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            raise NotAuthenticated

        return True


class IsAuthenticatedOrReadOnlyOrRaise401(IsAuthenticatedOrReadOnly):
    '''Пермишен с проверкой аутентификации и разрешений для пользователя'''

    def has_permission(self, request, view):
        if not super().has_permission(request, view):
            raise NotAuthenticated

        return True

from rest_framework.permissions import BasePermission

from foodgram.common.common_permissions import IsAuthenticatedOrRaise401, IsAuthenticatedOrReadOnlyOrRaise401


class ProfilePermission(BasePermission):
     '''Класс для определения прав доступа
        к профилю пользователя'''
     def has_permission(self, request, view):
        if view.action in ('me', 'set_password'):
            return IsAuthenticatedOrRaise401().has_permission(request, view)

        return IsAuthenticatedOrReadOnlyOrRaise401().has_permission(request, view)

from django.shortcuts import get_object_or_404
from djoser.views import UserViewSet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from foodgram.common.common_mixins import CreateAndDeleteObjectWithCurrentUserMixin
from foodgram.common.common_permissions import IsAuthenticatedOrRaise401
from recipes.paginators import PageNumberLimitPagination
from users.models import CustomUser
from . import errors
from .filters import RecipesLimitFilter
from .mixins import DisableDjoserUserActionsMixin
from .permissions import ProfilePermission
from .serializers import CustomUserSerializerWithRecipes
from .services import get_authors_user_is_following_with_recipes, add_author_follow, delete_author_follow


class CustomUserViewSet(DisableDjoserUserActionsMixin,
                        CreateAndDeleteObjectWithCurrentUserMixin,
                        UserViewSet):
    '''Вьюсет для работы с пользователями'''
    permission_classes = (ProfilePermission,)
    pagination_class = PageNumberLimitPagination
    filterset_class = RecipesLimitFilter

    serializer_class_for_objs_with_user = CustomUserSerializerWithRecipes
    recipes_limit_param_name = 'recipes_limit'

    @action(detail=False, methods=('GET',), url_path='subscriptions',
            serializer_class=CustomUserSerializerWithRecipes,
            permission_classes=(IsAuthenticatedOrRaise401,))
    def get_subscriptions(self, request):
        '''получение авторов, на которых подписан текущий пользователь'''
        authors = get_authors_user_is_following_with_recipes(request.user)
        authors = self.filter_queryset(authors)
        page = self.paginate_queryset(authors)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    @action(detail=True, methods=('POST', 'DELETE'), url_path='subscribe')
    def process_subscription(self, request, id=None):
        '''метод обработки создания или удаления подписки'''
        author = get_object_or_404(CustomUser, pk=id)
        if request.user == author:
            errors_ = {'POST': errors.USER_CANT_FOLLOW_HIMSELF,
                       'DELETE': errors.USER_CANT_UNFOLLOW_HIMSELF}
            return Response(errors_[request.method], status.HTTP_400_BAD_REQUEST)

        if request.method == 'POST':
            return self.create_with_user(add_author_follow,
                                         errors.USER_ALREADY_FOLLOWING_TO_THIS_AUTHOR)
        else:
            return self.delete_with_user(delete_author_follow,
                                         errors.USER_IS_NOT_FOllOWING_TO_THIS_AUTHOR)

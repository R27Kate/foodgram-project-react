from rest_framework import status
from rest_framework.response import Response


class CreateAndDeleteObjectWithCurrentUserMixin:
    '''Миксин для добавления и удаления объектов с проверкой
       текущего пользователя и отправлением сообщения об ошибке
       при неудачных операциях'''

    serializer_class_for_objs_with_user = None

    def create_with_user(self, adding_func, adding_error):
        obj_from_db = self.get_object()

        if not adding_func(obj_from_db, self.request.user):
            return Response(adding_error, status.HTTP_400_BAD_REQUEST)

        obj_to_return = self.serializer_class_for_objs_with_user(
            obj_from_db,
            context=self.get_serializer_context())
        return Response(obj_to_return.data, status.HTTP_201_CREATED)

    def delete_with_user(self, deleting_func, deleting_error):
        obj = self.get_object()

        if not deleting_func(obj, self.request.user):
            return Response(deleting_error, status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_204_NO_CONTENT)

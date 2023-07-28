from django.db import IntegrityError


def create_model_instance(model_class, **kwargs):
    '''Функция для создания экземляров модели'''
    try:
        model_class.objects.create(**kwargs)
    except IntegrityError:
        return False
    return True


def delete_model_instance(model_class, **kwargs):
    '''Функция для удаления экземляров модели'''
    deleted_count, _ = model_class.objects.filter(**kwargs).delete()
    return bool(deleted_count)

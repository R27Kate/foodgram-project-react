import re

from django.core.exceptions import ValidationError


def validate_username(username):
    '''проверка допустимости имени пользователя'''
    regex = r'[\w.@+-]+'
    if username == 'me':
        raise ValidationError('Username is invalid: "me"')

    invalid_symbols = ''.join(set(re.sub(regex, '', username)))
    if invalid_symbols:
        raise ValidationError(
            f'Сharacters errors {invalid_symbols} \
                'f' in username: "{username}"')

    return username


def check_int_is_positive(value):
    '''проверка, что число является положительным'''
    if value < 0:
        raise ValidationError('Value must be positive')
    return value

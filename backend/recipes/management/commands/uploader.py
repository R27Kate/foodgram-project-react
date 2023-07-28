import csv
from django.core.management.base import BaseCommand
from recipes.models import Ingredient
from foodgram.settings import CSV_DIR


class Command(BaseCommand):
    """Добавление ингредиентов в базу данных """

    help = 'Добавление ингредиентов в базу данных'

    def handle(self, *args, **kwargs):
        with open(
                f'{CSV_DIR}/ingredients.csv', encoding='utf-8'
        ) as file:
            reader = csv.reader(file)
            for row in reader:
                name, unit = row
                Ingredient.objects.get_or_create(name=name,
                                                 unit_of_measurement=unit)
        print('Список ингредиентов добавлен в базу данных')
        print('Добавлено', Ingredient.objects.count(), 'ингредиентов')

import csv

from django.core.management.base import BaseCommand

from foodgram.settings import CSV_DIR
from recipes.models import Tag


class Command(BaseCommand):
    """Добавление тэгов в базу данных """

    help = 'Загрузка тэгов в базу данных'

    def handle(self, *args, **kwargs):
        with open(
                f'{CSV_DIR}/tags.csv', encoding='utf-8'
        ) as file:
            csv_reader = csv.reader(file, delimiter=',', quotechar='"')
            for row in csv_reader:
                name = row[0]
                color = row[1]
                slug = row[2]
                Tag.objects.create(
                    name=name, color=color, slug=slug
                )
        print('Тэги в базу данных загружены')
        print('Добавлено', Tag.objects.count(), 'тэгов')

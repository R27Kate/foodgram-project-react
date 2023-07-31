# Foodgram - социальная сеть для публикации рецептов.

## Описание проекта
Дипломный проект Яндекс.Практикум/ Курс Python-разработчик.
Пользователи могут регистрироваться, авторизовываться, создавать публикации с рецептами, в которых описываются ингредиенты и их количество, подробное описание рецепта, время приготовления. Так же пользователь может загрузить фотографию рецепта и поставить тэг. По тегам возможна фильтрация. Рецепты фильтруются по пользователям. Есть функционал подписки на авторов, рецепты можно добавлять в избранное. Автор может изменять и удалять свой рецепт. Так же у данного проекта есть особенность: пользователь может выгрузить "Список покупок", в котором будет указаны ингредиенты и их количество для приготовления нужного рецепта. Если нужно приготовить несколько блюд по разным рецептам и ингредиенты будут пересекаться у этих рецептов, то в списке покупок они будут суммироваться.

## Технологии

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)
![Gunicorn](https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)



## Установка проекта на локальный компьютер из репозитория 
 - Клонировать репозиторий `git clone <адрес репозитория>`
 - перейти в директорию с клонированным репозиторием
 - установить виртуальное окружение `python3 -m venv venv`


## Создайте файл .env и заполните его своими данными:

   #Database
   SQL_USER=[имя_пользователя_базы]
   SQL_PASSWORD=[пароль_к_базе]
   SQL_DB=[имя_базы_данных]
   SQL_PORT=[порт_соединения_к_базе]
   SQL_HOST=[db]

   #Dganjo
   SECRET_KEY='SECRET_KEY'
   DEBUG=False
   ALLOWED_HOSTS='ваш домен'

 
## Автор
Екатерина Рагуткина - [GitHub](https://github.com/R27Kate)


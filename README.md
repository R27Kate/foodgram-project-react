# Foodgram - социальная сеть для публикации рецептов.
## Сведения о проекте для проверки
Проект доступен по адресу: https://foodgrampro.gotdns.ch/, IP: 51.250.23.63

Тестовые данные для админки:
логин: admin@admin.ru
пароль: 123ad123

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

##  Запуск проекта на удаленном сервере

1. На сервере создайте директорию foodgram/ : `sudo mkdir foodgram`.

2. В этой папке foodgram/ создайте файл .env: `sudo nano .env` и заполните его своими данными:
POSTGRES_DB=foodgram
POSTGRES_USER=foodgram_user
POSTGRES_PASSWORD=foodgram_password
DB_NAME=foodgram

#Dganjo
SECRET_KEY='SECRET_KEY'
DEBUG=False
ALLOWED_HOSTS='ваш домен'

DB_HOST=database host
DB_PORT=database port


4. Установите на сервер Nginx: `sudo apt install nginx -y` и запустите его: `sudo systemctl start nginx`. Настройте конфигурацию nginx: `sudo nano etc/nginx/sites-enabled/default`, например:

    ```
        server {
            server_name <Ваш IP> <Домен вашего сайта>;
            server_tokens off;
        
            location / {
                proxy_set_header Host $http_host;
                proxy_pass http://127.0.0.1:8000;
        }
    ```
Для настройки безопасного SSL-соединения получите SSL-сертификат: `sudo certbot --nginx`.

5. Добавьте в Settings->Secrets and variables->Actions своего проекта на GitHub следущие параметры

``` DOCKER_USERNAME=<ваш username на docker_hub>
    DOCKER_PASSWORD=<ваш пароль на docker_hub>
    POSTGRES_USER=<ваш username базы данных из .env файла>
    POSTGRES_PASSWORD=<ваш пароль базы данных из .env файла>
    POSTGRES_DB=<ваше имя базы данных из .env файла>
    DB_HOST=<ваш хост базы данных из .env файла>
    DB_PORT=<ваш порт базы данных из .env файла>
    SSH_KEY=<содержимое текстового файла с закрытым SSH-ключом>
    SSH_PASSPHRASE=<passphrase для SSH-ключа (пароль для входа на сервер)>
    USER=<ваше имя пользователя для вашего удаленного сервера>
    HOST=<IP-адрес для вашего удаленного сервера>
    ALLOWED_HOSTS=<ваши хосты из .env файла>
    TELEGRAM_TO=<ID вашего телеграм-аккаунта, узнать свой ID можно у телеграм-бота @userinfobot>
    TELEGRAM_TOKEN=<токен вашего бота, получить этот токен можно у телеграм-бота @BotFather.>
```

6. Выполните запуск workflow, чтобы автоматически развернуть проект на удаленном сервере:

```
  git add .
  git commit -m '<ваш коммит>'
  git push
```
 
## Автор
Екатерина Рагуткина - [GitHub](https://github.com/R27Kate)


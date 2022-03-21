# mmetrograd

Behold My Awesome Project!

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

МУП МЕТРОГРАД (ДИПЛОМНАЯ РАБОТА)
Эндпоинты:

    Регистрация пользователя (POST - 201):

    http://127.0.0.1:8000/auth/users/

        data (json):

           {
               "username": "new_user_1",
               "password": "bhoeh983yi",
               "email": "test@mail.ru"
           }

        response:

           {
               "username": "new_user_1",
               "email": "test@mail.ru",
               "id": "2",
           }


    Авторизация пользователя (POST - 200/400):

     http://127.0.0.1:8000/auth/token/login

        data(json):

        {
             "username": "neww2",
             "password": "bhoeh983yi"
        }

        response:

        {
            "auth_token": "f116ac210be2ab15bcba57beaa5781772b4ec9cf"
        }


    Список заявок пользователя (GET - 200/404):

    http://127.0.0.1:8000/tenant/{user_username}/tasks

        response:

        {
            "id": 1,
            "tasks": [
                {
                    "id": 1,
                    "inn": "23123123123123123"
                }
            ]
        }

        user_username тянется с формы авторизации


    Вывод одной заявки (GET - 200):

    http://127.0.0.1:8000/tenant/{user_username}/?task_id=1

        response:

        {
            "id": 1,
            "tasks": [
                {
                    "id": 1,
                    "inn": 123123,
                    "ogrn": 123123,
                    "individual_entrepreneur": false,
                    "individual": true,
                    "egr": true,
                    "license": true,
                    "address": "1qqwqdq",
                    "activity": "qdqwdqwd",
                    "term": "123 qadqd",
                    "create_at": "2022-03-06",
                    "fio": "qwdeqwdq qwdqwd",
                    "phone": "13131",
                    "passport": 123123,
                    "tenant": 1
                }
           ]
        }

id таски берется из списка заявок

в приложении можно не выводить "tenant": 1

    Удаление заявки по id (DELETE - 204):

    http://127.0.0.1:8000/tenant/{user_username}/delete-task/?task_id=1


    Создание заявки (POST - 201):

    http://127.0.0.1:8000/tenant/{user__username}/create-task/

        data(json):

           {
             "inn": 0,
             "ogrn": 0,
             "individual_entrepreneur": true,
             "individual": true,
             "egr": true,
             "license": true,
             "address": "string",
             "activity": "string",
             "term": "string",
             "fio": "string",
             "phone": "string",
             "passport": 0,
             "tenant": 0
           }

        "tenant": 0 - это id пользователя(таблица АРЕНДАТОР)

        response:

        {
            "id": 2,
            "inn": 0,
            "ogrn": 0,
            "individual_entrepreneur": true,
            "individual": true,
            "egr": true,
            "license": true,
            "address": "string",
            "activity": "string",
            "term": "string",
            "create_at": "2022-03-06",
            "fio": "string",
            "phone": "string",
            "passport": 0,
            "tenant": 2
        }

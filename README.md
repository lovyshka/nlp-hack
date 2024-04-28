## Структура проекта

docker-template
    ├── certbot  - настройка для ssl сертификатов
    │   └── conf
    │       ├── live
    │       │   └── naeb.tech
    │       ├── options-ssl-nginx.conf
    │       └── ssl-dhparams.pem
    ├── docker-compose.prod.yml 
    ├── docker-compose.yml
    ├── init-letsencrypt.sh
    ├── nginx
    │   ├── Dockerfile
    │   └── nginx.conf
    ├── postgres_data  [error opening dir]
    ├── README.md
    └── tmp
        ├── Dockerfile
        ├── Dockerfile.prod
        ├── entrypoint.prod.sh
        ├── entrypoint.sh
        ├── main
        │   ├── admin.py
        │   ├── apps.py
        │   ├── __init__.py
        │   ├── management
        │   │   ├── commands
        │   │   │   ├── bot.py
        │   │   │   └── __init__.py
        │   │   ├── __init__.py
        │   │   └── __pycache__
        │   │       └── __init__.cpython-310.pyc
        │   ├── migrations
        │   │   ├── 0001_initial.py
        │   │   ├── 0002_alter_customuser_options_customuser_telegram_chat_id_and_more.py
        │   │   └── __init__.py
        │   ├── models.py
        │   ├── __pycache__
        │   │   ├── apps.cpython-311.pyc
        │   │   ├── __init__.cpython-311.pyc
        │   │   ├── models.cpython-311.pyc
        │   │   └── views.cpython-311.pyc
        │   ├── templates
        │   │   ├── root.html
        │   │   ├── table.html
        │   │   └── to_render.html
        │   ├── tests.py
        │   └── views.py
        ├── manage.py
        ├── requirements.txt
        └── tmp
            ├── asgi.py
            ├── __init__.py
            ├── __pycache__
            │   ├── __init__.cpython-311.pyc
            │   ├── settings.cpython-311.pyc
            │   └── urls.cpython-311.pyc
            ├── settings.py
            ├── urls.py
            └── wsgi.py

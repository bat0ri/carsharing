


# Каршеринг DJANGO app

Этот проект представляет собой онлайн сервис для каршеринга, написанный на Django. В нем реализованы основные функции для аренды автомобилей.

## Функциональность проекта:

1. **FBV & CBV:**
   - Использование как функциональных, так и классовых представлений для обработки запросов.

2. **Mixin:**
   - Применение Mixin для заголовков страниц.

3. **Кастомный QuerySet:**
   - Реализация кастомного QuerySet для работы с корзиной.

4. **Celery:**
   - Использование Celery для асинхронной отправки писем пользователю в целях подтверждения. Брокер Redis

5. **Кэширование на Redis:**

## Запуск проекта

### 1. Установка зависимостей

Перед запуском проекта убедитесь, что у вас установлен Python и pip. 

```bash
python -m venv venv \
source venv/bin/activate
```
Затем выполните следующую команду для установки зависимостей:

```bash
pip install -r requirements.txt
```

### 2. Применение миграций
Если у вас есть локальный постгресс и редис, то отредактируйте парметры подключения к ним в Cars.settings.
Или же поднимите докеры:

```bash
docker-compose up -d
```

Выполните миграции для создания необходимых таблиц в базе данных:

```bash
python manage.py migrate
```
#### 2.1 Применение фикстур
```bash
./manage.py loaddata catalog/fixtures/category.json \
./manage.py loaddata catalog/fixtures/cars.json 
```

### 3. Создание административного аккаунта

Создайте аккаунт администратора для доступа к админ-панели:

```bash
python manage.py createsuperuser
```

### 4. Запуск сервера

Теперь вы можете запустить сервер с помощью следующей команды:

```bash
python manage.py runserver
```

Сервер будет доступен по адресу [http://localhost:8000/](http://localhost:8000/).

## Доступ к админ-панели

1. Перейдите по адресу [http://localhost:8000/admin/](http://localhost:8000/admin/).
2. Войдите, используя созданный вами аккаунт администратора.

## Референсы
+ [Initial Server Setup with Ubuntu 22.04](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-22-04)
+ [How To Set Up Django with Postgres, Nginx, and Gunicorn on Ubuntu 22.04](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-22-04)
+ [Redis cache backend for Django](https://github.com/jazzband/django-redis)
+ [environ docs](https://django-environ.readthedocs.io/en/latest/quickstart.html)
+ [celery docs](https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html)

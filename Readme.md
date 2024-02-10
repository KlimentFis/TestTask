# Тестовое задание Fastapi

## Установка

Клонирование и переход в папку проекта:
```shell
git clone https://github.com/KlimentFis/TestTask && cd TestTask
```

Установка и активация виртуального окружения (Не обязательно):
```shell
python -m venv venv && venv\Scripts\activate.bat
```

Установка зависимостей:
```shell
pip install -r requerements.txt
```

Создание миграций:
```shell
python manage.py makemigrations
```

Проведение миграций:
```shell
python manage.py migrate
```

Создание Супер-пользователя:
```shell
python manage.py createsuperuser
```

Запуск проекта:
```shell
python manage.py runserver
```

Загрузка постов делается через админ панель по адресу /admin

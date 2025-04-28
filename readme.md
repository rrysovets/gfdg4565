# Проект на Django с PostgreSQL

## Требования к окружению

- Python 3.8+
- Django (последняя стабильная версия)
- PostgreSQL 12+ с поддержкой JSONB
- Git

## Зависимости

Основные зависимости:
- `psycopg2` — драйвер PostgreSQL для Django
- `django-environ` — управление переменными окружения

Клиентская часть:
- `jQuery` — для динамических элементов интерфейса

## Настройка окружения

1. Установите Ubuntu 20.04+ (рекомендуется использовать [официальный образ](https://ubuntu.com/download) или [предварительно настроенный образ от OSBoxes](https://www.osboxes.org/ubuntu/))

2. Установите необходимые пакеты:

sudo apt update
sudo apt install python3-pip postgresql postgresql-contrib git

## Настройка базы данных
sudo -u postgres psql -c "CREATE DATABASE postgres;"
sudo -u postgres psql -c "CREATE USER root WITH PASSWORD 'root';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE postgres TO root;"
sudo -u postgres psql -c "ALTER DATABASE postgres OWNER TO root;"

## Установка проекта

python -m pip install --upgrade pip
pip install -r requirements.txt

## Запуск сервера

python manage.py runserver
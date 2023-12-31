# Cosmic Observatory Database Interface

## Описание

Этот проект представляет собой графический интерфейс базы данных космических наблюдений. Он объединяет данные из различных источников и предоставляет удобные инструменты для их обработки и анализа без необходимости знаний в программировании.

## Предварительные требования

Перед запуском убедитесь, что на вашей машине установлены:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Настройка переменных окружения

Для настройки переменных окружения нужно создать файл `.env`.
Либо использовать файл `.env.example`.

    cp .env.example .env

[//]: # ()
[//]: # (Создайте `.env` файл в корне проекта с необходимыми переменными окружения:)

[//]: # ()
[//]: # (```env)

[//]: # (# .env)

[//]: # (POSTGRES_USER=cosmic_user)

[//]: # (POSTGRES_PASSWORD=cosmic_password)

[//]: # (POSTGRES_DB=cosmic_db)

[//]: # (DATABASE_URL=postgresql://cosmic_user:cosmic_password@db/cosmic_db)

[//]: # (```)

### Запуск с помощью Docker Compose

Пересборка и запуск контейнера.

    docker compose up --build

Для запуска приложения и связанных с ним сервисов используйте следующую команду:

    docker compose up --build -d

Эта команда соберёт и запустит все необходимые контейнеры в фоновом режиме.

### Выполнение миграций базы данных

Для применения миграций базы данных выполните следующую команду:

    docker compose exec web alembic upgrade head

Если же необходимо автоматически сгенерировать миграцию, на основе существующей схемы, то нужно:
1. обновить файл `alembic/env.py` - если добавили новые модели, проверьте что они импортируются
2. запустить команду

    docker compose exec web alembic revision --autogenerate -m '<описание миграции>'


### Проверка работоспособности

Откройте веб-браузер и перейдите по адресу `http://localhost:8000` для доступа к API.

Интерфейс GraphQL будет доступен по адресу `http://localhost:8000/graphql`.

[//]: # (## Тестирование)

[//]: # ()
[//]: # (Для запуска тестов используйте следующую команду:)

[//]: # ()
[//]: # (```bash)

[//]: # (docker-compose exec web pytest)

[//]: # (```)

## Остановка и удаление контейнеров

Для остановки и удаления всех связанных контейнеров (и сетей), созданных с помощью Docker Compose, выполните:

    docker compose down

Для удаления ещё volumes, нужно использовать флаг `-v`.

    docker compose down -v

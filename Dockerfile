# Используйте официальный базовый образ Python
FROM python:3.12-slim

# Установите рабочий каталог в /app
WORKDIR /app

# Скопируйте файл зависимостей в рабочий каталог
COPY ./app/requirements.txt /app/requirements.txt

# Установите зависимости
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Скопируйте исходный код приложения в рабочий каталог
COPY ./app /app

# Укажите команду для запуска приложения
CMD ["uvicorn", "app", "--host", "0.0.0.0", "--port", "8000"]

# Откройте порт 8000
EXPOSE 8000

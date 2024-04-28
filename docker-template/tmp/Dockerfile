# Выбор базового образа
FROM python:3.10

# Установка рабочей директории в контейнере
WORKDIR /usr/src/app

# Установка переменных среды
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Установка зависимостей системы
RUN apt-get update && apt-get install -y \
    build-essential \
    libopenblas-dev \
    libfreetype6-dev \
    libpq-dev \
    libjpeg-dev \
    zlib1g-dev \
    libwebp-dev \
    libtiff5-dev \
    tk-dev \
    tcl-dev \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Установка PyTorch
RUN pip3 install torch --extra-index-url https://download.pytorch.org/whl/cu102

# Копирование и установка зависимостей Python
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# Копирование всего проекта
COPY . .

# Запуск entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

# TestTask_260324
Effective Mobile Тестовое задание на позицию DevOps

## Запуск Проекта

1. Требования к запуску 
    - Docker 
    - Docker Compose
2. Сборка - `docker-compose build` / `docker compose build`
3. Запуск - `docker-compose up` / `docker compose up`

## Конфигурация

На примере .env-example - для конфигурации - нужно создать env файл `.env`, в нем можно прописать порт на котором будет подниматься nginx и текст который будет выведен приложением.

По умолчанию эти переменные принимают следующие значения:
- NGINX_PORT=80
- HELLO_TEXT="Hello from Effective Mobile!"

## Архитектура 

Проект представляет собой два контейнера под управлением Docker Compose.

**nginx** — reverse proxy, принимает входящие HTTP-запросы и проксирует их
на бэкенд. Является единственной точкой входа снаружи.

**app** — Python FastAPI приложение, обрабатывает запросы от nginx.
Порт наружу не открыт, доступен только внутри docker-сети.


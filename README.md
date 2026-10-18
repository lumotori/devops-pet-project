# DevOps Pet Project

Небольшое FastAPI-приложение для практики DevOps.

## API

- `GET /` — возвращает приветствие.
- `GET /health` — сообщает, что приложение работает.

## Состав проекта

- `app/` — код приложения.
- `tests/` — автоматические тесты.
- `Dockerfile` и `docker-compose.yml` — сборка и запуск через Docker.
- `.github/workflows/ci.yml` — автоматический запуск тестов на GitHub.
- `k8s/` — Kubernetes-манифесты.
- `helm/devops-pet-project/` — Helm chart.

## CI

GitHub Actions запускает тесты при отправке изменений и при создании pull request.

## Локальный запуск

Для запуска понадобятся Docker, kubectl, kind и Helm. Эти команды выполняются в терминале Linux/WSL, а не на сайте GitHub.

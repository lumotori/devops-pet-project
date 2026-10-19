# DevOps pet project

[![CI](https://github.com/lumotori/devops-pet-project/actions/workflows/ci.yml/badge.svg)](https://github.com/lumotori/devops-pet-project/actions/workflows/ci.yml)

Небольшой API-сервис на FastAPI для практики DevOps-процесса: автоматических тестов, Docker, GitHub Actions, Kubernetes и Helm.

## Возможности

- `GET /` возвращает приветствие.
- `GET /health` возвращает статус приложения.
- Pytest проверяет ответы API.
- Docker Compose собирает и запускает приложение локально.
- GitHub Actions запускает тесты при отправке изменений и создании pull request.
- Helm chart развёртывает приложение в локальном Kubernetes-кластере kind.

## Технологии

- Python 3.12
- FastAPI и Uvicorn
- Pytest и FastAPI TestClient
- Docker и Docker Compose
- GitHub Actions
- Kubernetes, kind и Helm

## Схема проекта

```mermaid
flowchart LR
    Code[Изменения в коде] --> GitHub[Репозиторий GitHub]
    GitHub --> CI[GitHub Actions: установка зависимостей и запуск pytest]

    Source[Локальный проект] --> Compose[Docker Compose]
    Source --> Image[Образ Docker]
    Image --> Kind[Локальный кластер kind]
    Helm[Helm chart] --> Kind
    Kind --> Service[Service типа ClusterIP]
    Service --> API[Приложение FastAPI]

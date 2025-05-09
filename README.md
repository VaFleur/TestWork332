# TestWork332

## Запуск локально

### 1. Клонируйте репозиторий
```bash
git clone https://github.com/VaFleur/TestWork332.git
cd TestWork332
```

### 2. Установите зависимости
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Настройте переменные окружения
Заполните .env файл в корне проекта
```plaintext
API_KEY=your_api_key
DATABASE_URL=postgresql://user:password@localhost:5432/transactions
CELERY_BROKER_URL=redis://localhost:6379/0
```

### 4. Запустите PostgreSQL и Redis
Убедитесь, что PostgreSQL и Redis запущены на вашем локальном хосте.

### 5. Запустите FastAPI приложение
```bash
uvicorn app.main:app --reload
```
Приложение доступно по адресу:
```
http://localhost:8000
```
Swagger документация доступна по адресу:
```commandline
http://localhost:8000/docs
```

### 6. Запустите Celery worker
```bash
celery -A app.tasks.celery_app worker --loglevel=info
```

## Запуск с использованием Docker Compose

### 1. Клонируйте репозиторий
```bash
git clone https://github.com/VaFleur/TestWork332.git
cd TestWork332
```

### 2. Настройте переменные окружения
Заполните .env файл в корне проекта
```plaintext
API_KEY=your_api_key
DATABASE_URL=postgresql://user:password@localhost:5432/transactions
CELERY_BROKER_URL=redis://localhost:6379/0
```

### 3. Запустите контейнеры
```bash
docker compose up --build
```

Приложение доступно по адресу:
```
http://localhost:8000
```
Swagger документация доступна по адресу:
```commandline
http://localhost:8000/docs
```

## Запуск тестов

### Локально
```bash
pytest
```

### С использованием Docker Compose
```bash
docker compose exec app pytest
```
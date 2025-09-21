# 🐳 Docker Quick Start Guide

## Быстрый запуск

### Windows (PowerShell):
```powershell
.\start.ps1
```

### Linux/Mac (Bash):
```bash
chmod +x start.sh
./start.sh
```

### Ручной запуск:
```bash
docker-compose up --build
```

## 🔧 Полезные команды

### Управление контейнерами:
```bash
# Запуск в фоновом режиме
docker-compose up -d

# Остановка всех сервисов
docker-compose down

# Перезапуск сервисов
docker-compose restart

# Просмотр логов
docker-compose logs -f

# Просмотр статуса
docker-compose ps
```

### Выполнение команд в контейнерах:
```bash
# Django shell
docker-compose exec backend python manage.py shell

# Создание суперпользователя
docker-compose exec backend python manage.py createsuperuser

# Миграции
docker-compose exec backend python manage.py migrate

# Создание тестовых данных
docker-compose exec backend python manage.py create_test_data --clear

# Очистка данных
docker-compose exec backend python manage.py clear_data --confirm
```

### Управление данными:
```bash
# Очистка всех данных (включая базу данных)
docker-compose down -v

# Пересборка образов
docker-compose build --no-cache
```

## 🌐 Доступ к приложению

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000/api
- **Admin Panel**: http://localhost:8000/admin

## 👤 Тестовые аккаунты

- **Администратор**: admin / admin123
- **Пользователь**: user / user123

## 🐛 Решение проблем

### Порт уже используется:
```bash
# Остановить все контейнеры
docker-compose down

# Проверить какие процессы используют порты
netstat -tulpn | grep :3000
netstat -tulpn | grep :8000
```

### Проблемы с базой данных:
```bash
# Пересоздать базу данных
docker-compose down -v
docker-compose up --build
```

### Очистка Docker:
```bash
# Удалить все неиспользуемые контейнеры и образы
docker system prune -a

# Удалить все volumes
docker volume prune
```

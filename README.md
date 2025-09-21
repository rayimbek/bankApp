# Bank App

Веб-приложение для просмотра банков с функциональностью сортировки, фильтрации и управления.

## 🚀 Технологии

- **Frontend**: Nuxt 3 + TypeScript + Tailwind CSS
- **Backend**: Django REST Framework + PostgreSQL
- **Authentication**: JWT токены
- **Deployment**: Docker + Docker Compose

## 📋 Функциональность

### Для пользователей:
- 📊 Просмотр списка банков
- 🔍 Поиск и фильтрация банков
- 📈 Сортировка по различным параметрам
- 👤 Регистрация и авторизация
- 📱 Адаптивный дизайн

### Для администраторов:
- ➕ Добавление новых банков
- ✏️ Редактирование существующих банков
- 🗑️ Удаление банков
- 📊 Управление пользователями
- 🔧 Расширенная панель управления

## 🐳 Быстрый запуск с Docker

### Предварительные требования:
- Docker
- Docker Compose

### Запуск проекта:

```bash
# Клонируйте репозиторий
git clone <repository-url>
cd bank-app

# Запустите все сервисы
docker-compose up --build

# Или в фоновом режиме
docker-compose up -d --build
```

### Доступ к приложению:
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000/api
- **Admin Panel**: http://localhost:8000/admin

### Тестовые данные:
При первом запуске автоматически создаются:
- **Администратор**: admin / admin123
- **Пользователь**: user / user123
- **10 тестовых банков**

## 🛠️ Разработка без Docker

### Backend (Django):

```bash
cd backend

# Создайте виртуальное окружение
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate      # Windows

# Установите зависимости
pip install -r requirements.txt

# Настройте базу данных
python manage.py migrate

# Создайте тестовые данные
python manage.py create_test_data --clear

# Запустите сервер
python manage.py runserver
```

### Frontend (Nuxt):

```bash
cd frontend

# Установите зависимости
npm install

# Запустите сервер разработки
npm run dev
```

## 📁 Структура проекта

```
bank-app/
├── backend/                 # Django API
│   ├── accounts/           # Модуль пользователей
│   ├── banks/              # Модуль банков
│   ├── core/               # Настройки Django
│   └── requirements.txt    # Python зависимости
├── frontend/               # Nuxt приложение
│   ├── app/
│   │   ├── pages/          # Страницы
│   │   ├── layouts/        # Макеты
│   │   └── middleware/     # Middleware
│   ├── components/         # Vue компоненты
│   ├── stores/             # Pinia stores
│   └── package.json        # Node зависимости
├── docker-compose.yml      # Docker конфигурация
└── README.md              # Документация
```

## 🔧 Команды Docker

```bash
# Запуск всех сервисов
docker-compose up

# Запуск в фоновом режиме
docker-compose up -d

# Пересборка образов
docker-compose up --build

# Остановка сервисов
docker-compose down

# Просмотр логов
docker-compose logs -f

# Просмотр статуса
docker-compose ps

# Выполнение команд в контейнерах
docker-compose exec backend python manage.py shell
docker-compose exec frontend npm run build
```

## 🗄️ Управление данными

### Создание тестовых данных:
```bash
# В контейнере backend
docker-compose exec backend python manage.py create_test_data --clear

# Или локально
cd backend
python manage.py create_test_data --clear
```

### Очистка данных:
```bash
# В контейнере backend
docker-compose exec backend python manage.py clear_data --confirm

# Или локально
cd backend
python manage.py clear_data --confirm
```

## 🔐 Аутентификация

### API Endpoints:
- `POST /api/auth/register/` - Регистрация
- `POST /api/auth/login/` - Вход в систему
- `GET /api/banks/` - Список банков
- `GET /api/banks/{id}/` - Детали банка

### Тестовые аккаунты:
- **Администратор**: admin / admin123
- **Пользователь**: user / user123

## 📊 Сортировка и фильтрация

### Доступные параметры сортировки:
- **Название**: А-Я / Я-А
- **Лицензия**: По возрастанию / убыванию
- **Рейтинг**: Высокий / Низкий
- **Год основания**: Новые / Старые

### Фильтры:
- Поиск по названию и лицензии
- Фильтр по рейтингу
- Фильтр по статусу активности

## 🚀 Production развертывание

### Настройка для production:

1. **Обновите переменные окружения**:
```env
DEBUG=0
SECRET_KEY=your-secret-key
DATABASE_URL=postgresql://user:password@host:port/dbname
```

2. **Соберите статические файлы**:
```bash
docker-compose exec backend python manage.py collectstatic
```

3. **Используйте production веб-сервер**:
```dockerfile
# В Dockerfile для backend замените команду на:
CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]
```

## 🤝 Вклад в проект

1. Форкните репозиторий
2. Создайте ветку для новой функции
3. Внесите изменения
4. Создайте Pull Request

## 📝 Лицензия

MIT License

## 🐛 Решение проблем

### Ошибка с pywin32:
```bash
ERROR: Could not find a version that satisfies the requirement pywin32==306
```
**Решение**: Используется `requirements-docker.txt` вместо `requirements.txt` для исключения Windows-специфичных зависимостей.

### Ошибка с версией Node.js:
```bash
npm warn EBADENGINE package: 'nuxt@4.1.2', required: { node: '^20.19.0 || >=22.12.0' }
```
**Решение**: Nuxt 4 требует Node.js 20+. Используется `node:20-slim` в Dockerfile.

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
```~

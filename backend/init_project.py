#!/usr/bin/env python
"""
Скрипт для инициализации проекта с тестовыми данными
"""
import os
import sys
import django
from django.core.management import execute_from_command_line

def main():
    """Основная функция инициализации"""
    print("🚀 Инициализация проекта Bank App...")
    
    # Настройка Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    django.setup()
    
    try:
        # Применяем миграции
        print("📦 Применение миграций...")
        execute_from_command_line(['manage.py', 'migrate'])
        
        # Создаем суперпользователя если его нет
        print("👤 Проверка суперпользователя...")
        from django.contrib.auth import get_user_model
        User = get_user_model()
        
        if not User.objects.filter(is_superuser=True).exists():
            print("Создание суперпользователя...")
            User.objects.create_superuser(
                username='admin',
                email='admin@bankapp.com',
                password='admin123',
                first_name='Админ',
                last_name='Админов',
                role='admin'
            )
            print("✅ Суперпользователь создан: admin/admin123")
        else:
            print("✅ Суперпользователь уже существует")
        
        # Создаем тестовые данные
        print("🏦 Создание тестовых данных...")
        execute_from_command_line(['manage.py', 'create_test_data'])
        
        print("\n🎉 Инициализация завершена!")
        print("\n📋 Доступные учетные записи:")
        print("   👑 Админ: admin / admin123")
        print("   👤 Пользователь 1: user1 / user123")
        print("   👤 Пользователь 2: user2 / user123")
        print("   👤 Гость: guest / guest123")
        print("\n🌐 Запуск сервера: python manage.py runserver")
        
    except Exception as e:
        print(f"❌ Ошибка при инициализации: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()

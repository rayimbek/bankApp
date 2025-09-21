from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from banks.models import Bank

User = get_user_model()


class Command(BaseCommand):
    help = 'Очищает все тестовые данные'

    def add_arguments(self, parser):
        parser.add_argument(
            '--confirm',
            action='store_true',
            help='Подтвердить удаление всех данных',
        )

    def handle(self, *args, **options):
        if not options['confirm']:
            self.stdout.write(
                self.style.WARNING(
                    'ВНИМАНИЕ: Эта команда удалит ВСЕ данные!'
                )
            )
            self.stdout.write(
                'Используйте --confirm для подтверждения'
            )
            return

        self.stdout.write('Очистка всех данных...')
        
        # Удаляем всех пользователей кроме суперпользователей
        users_count = User.objects.filter(is_superuser=False).count()
        User.objects.filter(is_superuser=False).delete()
        self.stdout.write(f'Удалено пользователей: {users_count}')
        
        # Удаляем все банки
        banks_count = Bank.objects.count()
        Bank.objects.all().delete()
        self.stdout.write(f'Удалено банков: {banks_count}')
        
        self.stdout.write(
            self.style.SUCCESS('Все данные очищены!')
        )

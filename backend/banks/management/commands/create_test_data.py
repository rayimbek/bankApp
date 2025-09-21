from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from banks.models import Bank
from decimal import Decimal

User = get_user_model()


class Command(BaseCommand):
    help = 'Создает тестовые данные для банков и пользователей'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Очистить существующие данные перед созданием новых',
        )

    def handle(self, *args, **options):
        if options['clear']:
            self.stdout.write('Очистка существующих данных...')
            Bank.objects.all().delete()
            User.objects.filter(is_superuser=False).delete()
            self.stdout.write(
                self.style.SUCCESS('Существующие данные очищены')
            )

        self.create_test_users()
        self.create_test_banks()
        
        self.stdout.write(
            self.style.SUCCESS('Тестовые данные успешно созданы!')
        )

    def create_test_users(self):
        users_data = [
            {
                'username': 'admin',
                'email': 'admin@bankapp.com',
                'password': 'admin123',
                'first_name': 'Админ',
                'last_name': 'Админов',
                'role': 'admin',
                'is_staff': True,
                'is_superuser': True,
            },
            {
                'username': 'user1',
                'email': 'user1@bankapp.com',
                'password': 'user123',
                'first_name': 'Иван',
                'last_name': 'Иванов',
                'role': 'user',
            },
            {
                'username': 'user2',
                'email': 'user2@bankapp.com',
                'password': 'user123',
                'first_name': 'Петр',
                'last_name': 'Петров',
                'role': 'user',
            },
            {
                'username': 'guest',
                'email': 'guest@bankapp.com',
                'password': 'guest123',
                'first_name': 'Гость',
                'last_name': 'Гостев',
                'role': 'guest',
            }
        ]

        for user_data in users_data:
            user, created = User.objects.get_or_create(
                username=user_data['username'],
                defaults=user_data
            )
            if created:
                user.set_password(user_data['password'])
                user.save()
                self.stdout.write(f'Создан пользователь: {user.username}')
            else:
                self.stdout.write(f'Пользователь уже существует: {user.username}')

    def create_test_banks(self):
        banks_data = [
            {
                'name': 'Сбербанк России',
                'short_name': 'Сбербанк',
                'license_number': '1481',
                'address': 'г. Москва, ул. Вавилова, д. 19',
                'phone': '+7 (495) 500-55-50',
                'email': 'info@sberbank.ru',
                'website': 'https://www.sberbank.ru',
                'description': 'Крупнейший банк России и один из ведущих финансовых институтов мира.',
                'rating': Decimal('4.5'),
                'foundation_year': 1841,
                'is_active': True,
            },
            {
                'name': 'ВТБ',
                'short_name': 'ВТБ',
                'license_number': '1000',
                'address': 'г. Москва, ул. Большая Молчановка, д. 7',
                'phone': '+7 (495) 739-77-99',
                'email': 'info@vtb.ru',
                'website': 'https://www.vtb.ru',
                'description': 'Второй по величине банк России по размеру активов.',
                'rating': Decimal('4.2'),
                'foundation_year': 1990,
                'is_active': True,
            },
            {
                'name': 'Газпромбанк',
                'short_name': 'ГПБ',
                'license_number': '354',
                'address': 'г. Москва, ул. Наметкина, д. 16, стр. 1',
                'phone': '+7 (495) 913-55-55',
                'email': 'info@gazprombank.ru',
                'website': 'https://www.gazprombank.ru',
                'description': 'Один из крупнейших универсальных банков России.',
                'rating': Decimal('4.0'),
                'foundation_year': 1990,
                'is_active': True,
            },
            {
                'name': 'Альфа-Банк',
                'short_name': 'Альфа',
                'license_number': '1326',
                'address': 'г. Москва, ул. Каланчевская, д. 27',
                'phone': '+7 (495) 788-88-88',
                'email': 'info@alfabank.ru',
                'website': 'https://www.alfabank.ru',
                'description': 'Частный банк, входящий в топ-10 крупнейших банков России.',
                'rating': Decimal('4.3'),
                'foundation_year': 1990,
                'is_active': True,
            },
            {
                'name': 'Райффайзенбанк',
                'short_name': 'Райффайзен',
                'license_number': '3292',
                'address': 'г. Москва, ул. Троицкая, д. 17, стр. 1',
                'phone': '+7 (495) 363-36-33',
                'email': 'info@raiffeisen.ru',
                'website': 'https://www.raiffeisen.ru',
                'description': 'Российский банк, входящий в международную группу Raiffeisen Bank International.',
                'rating': Decimal('4.1'),
                'foundation_year': 1996,
                'is_active': True,
            },
            {
                'name': 'Тинькофф Банк',
                'short_name': 'Тинькофф',
                'license_number': '2673',
                'address': 'г. Москва, ул. Ходынский бульвар, д. 4',
                'phone': '+7 (800) 555-77-78',
                'email': 'info@tinkoff.ru',
                'website': 'https://www.tinkoff.ru',
                'description': 'Первый в России полностью онлайн банк.',
                'rating': Decimal('4.4'),
                'foundation_year': 2006,
                'is_active': True,
            },
            {
                'name': 'Россельхозбанк',
                'short_name': 'РСХБ',
                'license_number': '3349',
                'address': 'г. Москва, ул. Гагаринский переулок, д. 3',
                'phone': '+7 (495) 363-36-36',
                'email': 'info@rshb.ru',
                'website': 'https://www.rshb.ru',
                'description': 'Специализированный банк для развития агропромышленного комплекса России.',
                'rating': Decimal('3.8'),
                'foundation_year': 2000,
                'is_active': True,
            },
            {
                'name': 'МКБ',
                'short_name': 'МКБ',
                'license_number': '1978',
                'address': 'г. Москва, ул. Большая Ордынка, д. 16',
                'phone': '+7 (495) 363-36-36',
                'email': 'info@mkb.ru',
                'website': 'https://www.mkb.ru',
                'description': 'Московский кредитный банк - один из крупнейших частных банков России.',
                'rating': Decimal('4.0'),
                'foundation_year': 1992,
                'is_active': True,
            },
            {
                'name': 'ЮниКредит Банк',
                'short_name': 'ЮниКредит',
                'license_number': '1',
                'address': 'г. Москва, ул. Лесная, д. 9',
                'phone': '+7 (495) 258-99-99',
                'email': 'info@unicredit.ru',
                'website': 'https://www.unicredit.ru',
                'description': 'Российский банк, входящий в международную группу UniCredit.',
                'rating': Decimal('3.9'),
                'foundation_year': 1989,
                'is_active': True,
            },
            {
                'name': 'Почта Банк',
                'short_name': 'Почта Банк',
                'license_number': '650',
                'address': 'г. Москва, ул. Варшавское шоссе, д. 37',
                'phone': '+7 (495) 775-77-75',
                'email': 'info@postbank.ru',
                'website': 'https://www.postbank.ru',
                'description': 'Совместный проект Почты России и ВТБ.',
                'rating': Decimal('3.7'),
                'foundation_year': 2016,
                'is_active': True,
            }
        ]

        for bank_data in banks_data:
            bank, created = Bank.objects.get_or_create(
                license_number=bank_data['license_number'],
                defaults=bank_data
            )
            if created:
                self.stdout.write(f'Создан банк: {bank.name}')
            else:
                self.stdout.write(f'Банк уже существует: {bank.name}')

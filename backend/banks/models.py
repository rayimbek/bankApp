from django.db import models


class Bank(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название банка')
    short_name = models.CharField(max_length=100, verbose_name='Краткое название', blank=True)
    license_number = models.CharField(max_length=50, unique=True, verbose_name='Номер лицензии')
    address = models.TextField(verbose_name='Адрес')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Email')
    website = models.URLField(verbose_name='Веб-сайт', blank=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0, verbose_name='Рейтинг')
    foundation_year = models.IntegerField(verbose_name='Год основания')
    is_active = models.BooleanField(default=True, verbose_name='Активный')

    base_fields = ['id', 'name', 'short_name', 'license_number', 'rating', 'is_active']

    extended_fields = base_fields + ['address', 'phone', 'email', 'website', 'description', 'foundation_year']

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Банк'
        verbose_name_plural = 'Банки'
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.license_number})"

import django_filters
from .models import Bank

class BankFilter(django_filters.FilterSet):
    min_rating = django_filters.NumberFilter(field_name='rating', lookup_expr='gte')
    max_rating = django_filters.NumberFilter(field_name='rating', lookup_expr='lte')
    min_year = django_filters.NumberFilter(field_name='foundation_year', lookup_expr='gte')
    max_year = django_filters.NumberFilter(field_name='foundation_year', lookup_expr='lte')

    class Meta:
        model = Bank
        fields = {
            'name': ['icontains'],
            'license_number': ['exact'],
            'is_active': ['exact'],
        }
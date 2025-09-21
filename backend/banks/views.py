from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Bank
from .serializers import BankBaseSerializer, BankExtendedSerializer, BankAdminSerializer
from .filters import BankFilter


class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.filter(is_active=True)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = BankFilter
    search_fields = ['name', 'license_number', 'address']
    ordering_fields = ['name', 'rating', 'foundation_year']
    ordering = ['name']

    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_admin and self.action in ['create', 'update', 'partial_update', 'destroy']:
                return BankAdminSerializer
            return BankExtendedSerializer
        return BankBaseSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy', 'export']:
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]

    @action(detail=False, methods=['get'])
    def export(self, request):
        import pandas as pd
        from django.http import HttpResponse

        banks = Bank.objects.all()
        data = []
        for bank in banks:
            data.append({
                'Название': bank.name,
                'Лицензия': bank.license_number,
                'Адрес': bank.address,
                'Телефон': bank.phone,
                'Email': bank.email,
                'Рейтинг': float(bank.rating),
                'Год основания': bank.foundation_year,
            })

        df = pd.DataFrame(data)
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="banks_export.xlsx"'

        df.to_excel(response, index=False, engine='openpyxl')
        return response
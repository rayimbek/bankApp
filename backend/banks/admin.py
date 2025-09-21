from django.contrib import admin
from .models import Bank

@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ('name', 'license_number', 'rating', 'foundation_year', 'is_active')
    list_filter = ('is_active', 'rating', 'foundation_year')
    search_fields = ('name', 'license_number', 'address')
    list_editable = ('is_active', 'rating')
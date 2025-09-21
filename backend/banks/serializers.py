from rest_framework import serializers
from .models import Bank

class BankBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = Bank.base_fields

class BankExtendedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = Bank.extended_fields

class BankAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'

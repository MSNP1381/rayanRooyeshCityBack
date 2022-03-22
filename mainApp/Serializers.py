from rest_framework import serializers
from .models import Transaction,Sections


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

    def create(self, data):
        print(100*"%")
        print(data)
        return Transaction.objects.create(**data)


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sections
        fields = '__all__'
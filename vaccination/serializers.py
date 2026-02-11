from rest_framework import serializers
from .models import Vacinacao


class VacinacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacinacao
        fields = '__all__'

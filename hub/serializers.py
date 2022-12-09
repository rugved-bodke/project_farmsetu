from rest_framework import serializers
from .models import MinTemp, RainDays, Rainfall, Sunshine, MaxTemp, AirFrost, MeanTemp


class MinTempSerializer(serializers.ModelSerializer):
    class Meta:
        model = MinTemp
        fields = '__all__'
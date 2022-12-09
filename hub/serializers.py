from rest_framework import serializers
from .models import MinTemp, RainDays, Rainfall, Sunshine, MaxTemp, AirFrost, MeanTemp


class MinTempSerializer(serializers.ModelSerializer):
    class Meta:
        model = MinTemp
        fields = '__all__'

class RainDaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = RainDays
        fields = '__all__'

class RainfallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rainfall
        fields = '__all__'

class SunshineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sunshine
        fields = '__all__'  

class MaxTempSerializer(serializers.ModelSerializer):       
    class Meta:
        model = MaxTemp
        fields = '__all__'          

class AirFrostSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirFrost
        fields = '__all__'

class MeanTempSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeanTemp
        fields = '__all__'

        
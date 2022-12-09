from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import MinTemp, RainDays, Rainfall, Sunshine, MaxTemp, AirFrost, MeanTemp
from .serializers import MinTempSerializer, RainDaysSerializer, RainfallSerializer, SunshineSerializer, MaxTempSerializer, AirFrostSerializer, MeanTempSerializer

class MinTempView(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, format="json"):
        # get 10 most recent min_temp records
        min_temp = MinTemp.objects.all().order_by('-id')[:10]
        serializer = MinTempSerializer(min_temp, many=True)
        return Response(serializer.data)

class RainDaysView(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, format="json"):
        # get 10 most recent rain_days records
        rain_days = RainDays.objects.all().order_by('-id')[:10]
        serializer = RainDaysSerializer(rain_days, many=True)
        return Response(serializer.data)

class RainfallView(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, format="json"):
        # get 10 most recent rainfall records
        rainfall = Rainfall.objects.all().order_by('-id')[:10]
        serializer = RainfallSerializer(rainfall, many=True)
        return Response(serializer.data)

class SunshineView(APIView):  
    permission_classes = (permissions.AllowAny,)
    def get(self, request, format="json"):
        # get 10 most recent sunshine records
        sunshine = Sunshine.objects.all().order_by('-id')[:10]
        serializer = SunshineSerializer(sunshine, many=True)
        return Response(serializer.data)

class MaxTempView(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, format="json"):
        # get 10 most recent max_temp records
        max_temp = MaxTemp.objects.all().order_by('-id')[:10]
        serializer = MaxTempSerializer(max_temp, many=True)
        return Response(serializer.data)

class AirFrostView(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, format="json"):
        # get 10 most recent air_frost records
        air_frost = AirFrost.objects.all().order_by('-id')[:10]
        serializer = AirFrostSerializer(air_frost, many=True)
        return Response(serializer.data)

class MeanTempView(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, format="json"):
        # get 10 most recent mean_temp records
        mean_temp = MeanTemp.objects.all().order_by('-id')[:10]
        serializer = MeanTempSerializer(mean_temp, many=True)
        return Response(serializer.data)

        
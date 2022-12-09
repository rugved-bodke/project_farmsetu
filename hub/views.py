from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import MinTemp, RainDays, Rainfall, Sunshine, MaxTemp, AirFrost, MeanTemp
from .serializers import MinTempSerializer

class MinTempView(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, format="json"):
        # get 10 most recent min_temp records
        min_temp = MinTemp.objects.all().order_by('-id')[:10]
        serializer = MinTempSerializer(min_temp, many=True)
        return Response(serializer.data)

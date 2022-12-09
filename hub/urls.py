from django.urls import path, include
from .views import (MinTempView, MaxTempView, RainfallView, SunshineView, RainDaysView, AirFrostView, MeanTempView)

urlpatterns = [
    path('min_temp/', MinTempView.as_view()),
    path('max_temp/', MaxTempView.as_view()),
    path('rainfall/', RainfallView.as_view()),
    path('sunshine/', SunshineView.as_view()),
    path('rain_days/', RainDaysView.as_view()),
    path('air_frost/', AirFrostView.as_view()),
    path('mean_temp/', MeanTempView.as_view()),
]
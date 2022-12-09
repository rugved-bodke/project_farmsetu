from django.urls import path, include
from .views import (MinTempView)

urlpatterns = [
    path('min_temp/', MinTempView.as_view()),
]
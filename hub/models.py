from django.db import models
from django.contrib import admin

from hub.model.base import BaseModel
from hub.model.sunshine import Sunshine
from hub.model.rainfall import Rainfall
from hub.model.rain_days import RainDays
from hub.model.min_temp import MinTemp
from hub.model.max_temp import MaxTemp
from hub.model.air_frost import AirFrost
from hub.model.mean_temp import MeanTemp

admin.site.register(Sunshine)
admin.site.register(Rainfall)
admin.site.register(RainDays)
admin.site.register(MinTemp)
admin.site.register(MaxTemp)
admin.site.register(AirFrost)
admin.site.register(MeanTemp)
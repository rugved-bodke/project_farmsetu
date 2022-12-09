from django.db import models
from .base import BaseModel
class RainDays(BaseModel):
    class Meta:
        db_table = 'tbl_rain_days'

    
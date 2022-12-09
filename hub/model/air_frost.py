from django.db import models
from .base import BaseModel
class AirFrost(BaseModel):
    class Meta:
        db_table = 'tbl_air_frost'

    
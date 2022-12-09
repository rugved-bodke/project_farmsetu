from django.db import models
from .base import BaseModel
class MeanTemp(BaseModel):
    class Meta:
        db_table = 'tbl_mean_temp'

    
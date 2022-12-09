from django.db import models
from .base import BaseModel
class MinTemp(BaseModel):
    class Meta:
        db_table = 'tbl_min_temp'

    
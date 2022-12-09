from django.db import models
from .base import BaseModel
class MaxTemp(BaseModel):
    class Meta:
        db_table = 'tbl_max_temp'

    
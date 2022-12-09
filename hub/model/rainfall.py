from django.db import models
from .base import BaseModel
class Rainfall(BaseModel):
    class Meta:
        db_table = 'tbl_rainfall'

    
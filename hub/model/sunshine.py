from django.db import models
from .base import BaseModel
class Sunshine(BaseModel):
    class Meta:
        db_table = 'tbl_sunshine'

    
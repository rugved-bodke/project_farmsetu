from django.db import models
from .base import BaseModel

class Sunshine(BaseModel):
    date = models.DateField()
    class Meta:
        db_table = 'sunshine'

    
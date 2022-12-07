from django.db import models

class BaseModel(models.Model):
    """
    Base model for all sub models
    """
    name = models.CharField(max_length=255)
    class Meta:
        abstract = True

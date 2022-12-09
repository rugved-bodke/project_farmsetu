from django.db import models


class BaseModel(models.Model):
    jan = models.FloatField(default=0.0)
    jan_year = models.IntegerField(default=0)
    feb = models.FloatField(default=0.0)
    feb_year = models.IntegerField(default=0)
    mar = models.FloatField(default=0.0)
    mar_year = models.IntegerField(default=0)
    apr = models.FloatField(default=0.0)
    apr_year = models.IntegerField(default=0)
    may = models.FloatField(default=0.0)
    may_year = models.IntegerField(default=0)
    jun = models.FloatField(default=0.0)
    jun_year = models.IntegerField(default=0)
    jul = models.FloatField(default=0.0)
    jul_year = models.IntegerField(default=0)
    aug = models.FloatField(default=0.0)
    aug_year = models.IntegerField(default=0)
    sep = models.FloatField(default=0.0)
    sep_year = models.IntegerField(default=0)
    oct = models.FloatField(default=0.0)
    oct_year = models.IntegerField(default=0)
    nov = models.FloatField(default=0.0)
    nov_year = models.IntegerField(default=0)
    dec = models.FloatField(default=0.0)
    dec_year = models.IntegerField(default=0)
    winter = models.FloatField(default=0.0)
    winter_year = models.IntegerField(default=0)
    spring = models.FloatField(default=0.0)
    spring_year = models.IntegerField(default=0)
    summer = models.FloatField(default=0.0)
    summer_year = models.IntegerField(default=0)
    autumn = models.FloatField(default=0.0)
    autumn_year = models.IntegerField(default=0)
    annual = models.FloatField(default=0.0)
    annual_year = models.IntegerField(default=0)
    region = models.CharField(max_length=255, default='UK')


    class Meta:
        abstract = True



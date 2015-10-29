from django.db import models
from django.contrib.auth.models import User


class Crisis(models.Model):
    """
    Data for a given crisis. See the sample output of the
    API we plant to use:
    https://api.sigimera.org/v1/crises.json
    """

    title        = models.CharField(max_length=200)
    alert_level  = models.CharField(max_length=200)
    event_id     = models.IntegerField()
    created_date = models.DateTimeField()
    start_date   = models.DateTimeField()
    end_date     = models.DateTimeField()
    geo_lat      = models.FloatField()
    geo_long     = models.FloatField()


class CrisisUser(models.Model):
    user       = models.OneToOneField(User, on_delete=models.CASCADE)
    cellphone  = models.CharField(max_length=10, default='')
    address    = models.CharField(max_length=100, default='')
    #crisis     = models.ForeignKey(Crisis)
    notified   = models.BooleanField(default=False)
    evacuating = models.BooleanField(default=False)
    responded  = models.BooleanField(default=False)
from django.db import models

# Create your models here.
from django.db import models


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


class CrisisUsers(models.Model):
    # user       = models.ForeignKey(User)
    crisis     = models.ForeignKey(Crisis)
    notified   = models.BooleanField(default=False)
    evacuating = models.BooleanField(default=False)
    responded  = models.BooleanField(default=False)
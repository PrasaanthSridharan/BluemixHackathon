from django.db import models
from django.contrib.auth.models import User


class Crisis(models.Model):
    """
    Data for a given crisis. See the sample output of the
    API we plan to use:
    http://reliefweb.int/help/api/advanced

    Here are all the fields they provide:
    http://reliefweb.int/help/api/field-definitions#disaster
    """

    rwid         = models.IntegerField() #ReliefWeb Id
    name         = models.CharField(max_length=200)
    url          = models.CharField(max_length=200)
    status       = models.CharField(max_length=8,
                                    choices=[
                                    ("alert", "alert"),
                                    ("current", "current"),
                                    ("past", "past")])
    glide        = models.CharField(max_length=100) # GUID
    countries    = models.CharField(max_length=256) # CSV of ISO3 country names (sorted alphabetically)
    # geo_lat      = models.FloatField()
    # geo_long     = models.FloatField()

    def defineFromReliefWebResponse(self, data):
        self.rwid = data["fields"]["id"]
        self.name = data["fields"]["name"]
        self.url = data["fields"]["url"]
        self.status = data["fields"]["status"]
        self.glide = data["fields"]["glide"]

        countries = []
        for c in data["fields"]["country"]:
            countries.append(c["iso3"])
        self.countries = "".join(countries)

class CrisisUser(models.Model):
    user       = models.OneToOneField(User, on_delete=models.CASCADE)
    cellphone  = models.CharField(max_length=10, default='')
    address    = models.CharField(max_length=100, default='')
    country    = models.CharField(max_length=10)

class CrisisUserPairs(models.Model):
    user       = models.ForeignKey(CrisisUser)
    crisis     = models.ForeignKey(Crisis)
    notified   = models.BooleanField(default=False)
    evacuating = models.BooleanField(default=False)
    responded  = models.BooleanField(default=False)

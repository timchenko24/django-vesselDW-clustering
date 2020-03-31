from django.db import models

# Create your models here.
class VesselType(models.Model):
    id = models.UUIDField(primary_key=True, null=False, unique=True)
    type = models.CharField(max_length=50, null=False)


class VesselBuild(models.Model):
    id = models.UUIDField(primary_key=True, null=False, unique=True)
    year = models.IntegerField(null=False)
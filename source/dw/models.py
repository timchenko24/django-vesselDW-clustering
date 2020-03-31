from django.db import models

# Create your models here.
class VesselType(models.Model):
    id = models.UUIDField(primary_key=True, null=False, unique=True)
    type = models.CharField(max_length=50, null=False)


class VesselBuild(models.Model):
    id = models.UUIDField(primary_key=True, null=False, unique=True)
    year = models.IntegerField(null=False)


class VesselFlag(models.Model):
    id = models.UUIDField(primary_key=True, null=False, unique=True)
    flag = models.CharField(max_length=50, null=False)


class Vessel(models.Model):
    mmsi = models.IntegerField(primary_key=True, null=False, unique=True)
    type = models.ForeignKey(VesselType, on_delete=models.PROTECT, null=False)
    flag = models.ForeignKey(VesselFlag, on_delete=models.PROTECT, null=False)
    build = models.ForeignKey(VesselBuild, on_delete=models.PROTECT, null=False)
    name = models.CharField(max_length=70, null=False)
    imo = models.IntegerField()
    call_sign = models.CharField(max_length=10, null=False)
    length = models.IntegerField()
    width = models.IntegerField()
    grt = models.IntegerField()
    dwt = models.IntegerField()
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


class PortCountry(models.Model):
    id = models.UUIDField(primary_key=True, null=False, unique=True)
    name = models.CharField(max_length=50, null=False)


class Port(models.Model):
    id = models.UUIDField(primary_key=True, null=False, unique=True)
    country = models.ForeignKey(PortCountry, on_delete=models.PROTECT, null=False)
    name = models.CharField(max_length=50, null=False)
    type = models.CharField(max_length=15, null=False)
    longitude = models.DecimalField(max_digits=8, decimal_places=5, null=False)
    latitude = models.DecimalField(max_digits=8, decimal_places=5, null=False)


class Route(models.Model):
    id = models.UUIDField(primary_key=True, null=False, unique=True)
    departure_port = models.ForeignKey(Port, on_delete=models.PROTECT, null=False, related_name='dep_port')
    destination_port = models.ForeignKey(Port, on_delete=models.PROTECT, null=False, related_name='dest_port')


class Date(models.Model):
    id = models.UUIDField(primary_key=True, null=False, unique=True)
    minute = models.IntegerField(null=False)
    hour = models.IntegerField(null=False)
    weekday = models.CharField(max_length=15, null=False)
    day = models.IntegerField(null=False)
    month = models.IntegerField(null=False)
    quarter = models.IntegerField(null=False)
    year = models.IntegerField(null=False)


class Voyage(models.Model):
    id = models.UUIDField(primary_key=True, null=False, unique=True)
    route = models.ForeignKey(Route, on_delete=models.PROTECT, null=False)
    mmsi = models.ForeignKey(Vessel, on_delete=models.PROTECT, null=False)
    departure_date = models.ForeignKey(Date, on_delete=models.PROTECT, null=False, related_name='dep_date')
    arrival_date = models.ForeignKey(Date, on_delete=models.PROTECT, null=False, related_name='arr_date')
    time_in_port = models.IntegerField(null=False)
    fuel_costs = models.IntegerField(null=False)
    crew_costs = models.IntegerField(null=False)
    port_charges = models.IntegerField(null=False)
    insurance_costs = models.IntegerField(null=False)
    total_costs = models.IntegerField(null=False)
    cargo_income = models.IntegerField(null=False)
    net_total_freight = models.IntegerField(null=False)
    voyage_profit = models.IntegerField(null=False)
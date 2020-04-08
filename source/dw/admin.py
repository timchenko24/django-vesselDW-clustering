from django.contrib import admin
from django.apps import apps
from .models import *

# Register your models here.
@admin.register(VesselType)
class VesselTypeAdmin(admin.ModelAdmin):
    list_display = ('type',)
    list_display_links = ('type',)
    search_fields = ('type',)


@admin.register(VesselBuild)
class VesselBuildAdmin(admin.ModelAdmin):
    list_display = ('year',)
    list_display_links = ('year',)
    search_fields = ('year',)


@admin.register(VesselFlag)
class VesselFlagAdmin(admin.ModelAdmin):
    list_display = ('flag',)
    list_display_links = ('flag',)
    search_fields = ('flag',)


@admin.register(Vessel)
class VesselAdmin(admin.ModelAdmin):
    list_display = ('mmsi', 'type', 'flag', 'build', 'name', 'imo', 'call_sign', 'length', 'width', 'grt', 'dwt')
    list_display_links = ('type', 'flag', 'build', 'name', 'imo', 'call_sign', 'length', 'width', 'grt', 'dwt')
    search_fields = ('mmsi', 'type', 'flag', 'build', 'name', 'imo', 'call_sign', 'length', 'width', 'grt', 'dwt')


@admin.register(PortCountry)
class PortCountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)


@admin.register(Port)
class PortAdmin(admin.ModelAdmin):
    list_display = ('country', 'name', 'type', 'longitude', 'latitude')
    list_display_links = ('country', 'name', 'type', 'longitude', 'latitude')
    search_fields = ('country', 'name', 'type', 'longitude', 'latitude')


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('departure_port', 'destination_port')
    list_display_links = ('departure_port', 'destination_port')
    search_fields = ('departure_port', 'destination_port')


@admin.register(Date)
class DateAdmin(admin.ModelAdmin):
    list_display = ('minute', 'hour', 'weekday', 'day', 'month', 'quarter', 'year')
    list_display_links = ('minute', 'hour', 'weekday', 'day', 'month', 'quarter', 'year')
    search_fields = ('minute', 'hour', 'weekday', 'day', 'month', 'quarter', 'year')


@admin.register(Voyage)
class VoyageAdmin(admin.ModelAdmin):
    list_display = ('route', 'mmsi', 'departure_date', 'arrival_date', 'time_in_port', 'fuel_costs', 'crew_costs',
                    'port_charges', 'insurance_costs', 'total_costs', 'cargo_income', 'net_total_freight',
                    'voyage_profit')
    list_display_links = ('route', 'mmsi', 'departure_date', 'arrival_date', 'time_in_port', 'fuel_costs', 'crew_costs',
                          'port_charges', 'insurance_costs', 'total_costs', 'cargo_income', 'net_total_freight',
                          'voyage_profit')
    search_fields = ('route', 'mmsi', 'departure_date', 'arrival_date', 'time_in_port', 'fuel_costs', 'crew_costs',
                     'port_charges', 'insurance_costs', 'total_costs', 'cargo_income', 'net_total_freight',
                     'voyage_profit')
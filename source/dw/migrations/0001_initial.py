# Generated by Django 2.2.5 on 2020-03-31 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VesselBuild',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, unique=True)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='VesselFlag',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, unique=True)),
                ('flag', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='VesselType',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, unique=True)),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vessel',
            fields=[
                ('mmsi', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dw.VesselType')),
                ('flag', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dw.VesselFlag')),
                ('build', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dw.VesselBuild')),
                ('name', models.CharField(max_length=70)),
                ('imo', models.IntegerField()),
                ('call_sign', models.CharField(max_length=10)),
                ('length', models.IntegerField()),
                ('width', models.IntegerField()),
                ('grt', models.IntegerField()),
                ('dwt', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, unique=True)),
                ('minute', models.IntegerField()),
                ('hour', models.IntegerField()),
                ('weekday', models.CharField(max_length=15)),
                ('day', models.IntegerField()),
                ('month', models.IntegerField()),
                ('quarter', models.IntegerField()),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PortCountry',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Port',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, unique=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dw.PortCountry')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=15)),
                ('longitude', models.DecimalField(decimal_places=5, max_digits=8)),
                ('latitude', models.DecimalField(decimal_places=5, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, unique=True)),
                ('departure_port', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dep_port', to='dw.Port')),
                ('destination_port', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dest_port', to='dw.Port')),
            ],
        ),
        migrations.CreateModel(
            name='Voyage',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, unique=True)),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dw.Route')),
                ('mmsi', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dw.Vessel')),
                ('departure_date',
                 models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dep_date', to='dw.Date')),
                ('arrival_date',
                 models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='arr_date', to='dw.Date')),
                ('time_in_port', models.IntegerField()),
                ('fuel_costs', models.IntegerField()),
                ('crew_costs', models.IntegerField()),
                ('port_charges', models.IntegerField()),
                ('insurance_costs', models.IntegerField()),
                ('total_costs', models.IntegerField()),
                ('cargo_income', models.IntegerField()),
                ('net_total_freight', models.IntegerField()),
                ('voyage_profit', models.IntegerField()),
            ],
        ),
    ]
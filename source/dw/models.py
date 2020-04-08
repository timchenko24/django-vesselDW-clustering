from django.db import models


# Create your models here.
class VesselType(models.Model):
    id = models.UUIDField(primary_key=True, null=False, unique=True)
    type = models.CharField(max_length=50, null=False, verbose_name='Тип')

    def __str__(self):
        return self.type

    class Meta:
        verbose_name_plural = 'Типы судов'
        verbose_name = 'Тип судна'


class VesselBuild(models.Model):
    id = models.UUIDField(primary_key=True, null=False, unique=True)
    year = models.IntegerField(null=False, verbose_name='Год')

    def __str__(self):
        return str(self.year)

    class Meta:
        verbose_name_plural = 'Года постройки судов'
        verbose_name = 'Год постройки судна'


class VesselFlag(models.Model):
    id = models.UUIDField(primary_key=True, null=False, unique=True)
    flag = models.CharField(max_length=50, null=False, verbose_name='Флаг')

    def __str__(self):
        return self.flag

    class Meta:
        verbose_name_plural = 'Флаги судов'
        verbose_name = 'Флаг судна'


class Vessel(models.Model):
    mmsi = models.IntegerField(primary_key=True, null=False, unique=True, verbose_name='MMSI')
    type = models.ForeignKey(VesselType, on_delete=models.PROTECT, null=False, verbose_name='Тип')
    flag = models.ForeignKey(VesselFlag, on_delete=models.PROTECT, null=False, verbose_name='Флаг')
    build = models.ForeignKey(VesselBuild, on_delete=models.PROTECT, null=False, verbose_name='Год постройки')
    name = models.CharField(max_length=70, null=False, verbose_name='Название')
    imo = models.IntegerField(verbose_name='IMO')
    call_sign = models.CharField(max_length=10, null=False, verbose_name='Позывной')
    length = models.IntegerField(verbose_name='Длина')
    width = models.IntegerField(verbose_name='Ширина')
    grt = models.IntegerField(verbose_name='Грузоподъемность')
    dwt = models.IntegerField(verbose_name='Дедвейт')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Суда'
        verbose_name = 'Судно'


class PortCountry(models.Model):
    id = models.UUIDField(primary_key=True, null=False, unique=True)
    name = models.CharField(max_length=50, null=False, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Страны портов'
        verbose_name = 'Страна порта'


class Port(models.Model):
    id = models.UUIDField(primary_key=True, null=False, unique=True)
    country = models.ForeignKey(PortCountry, on_delete=models.PROTECT, null=False, verbose_name='Страна')
    name = models.CharField(max_length=50, null=False, verbose_name='Название')
    type = models.CharField(max_length=15, null=False, verbose_name='Тип')
    longitude = models.DecimalField(max_digits=8, decimal_places=5, null=False, verbose_name='Долгота')
    latitude = models.DecimalField(max_digits=8, decimal_places=5, null=False, verbose_name='Широта')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Порты'
        verbose_name = 'Порт'


class Route(models.Model):
    id = models.UUIDField(primary_key=True, null=False, unique=True)
    departure_port = models.ForeignKey(Port, on_delete=models.PROTECT, null=False, related_name='dep_port',
                                       verbose_name='Порт отправления')
    destination_port = models.ForeignKey(Port, on_delete=models.PROTECT, null=False, related_name='dest_port',
                                         verbose_name='Порт назначения')

    def __str__(self):
        return '{0} - {1}'.format(self.departure_port, self.destination_port)

    class Meta:
        verbose_name_plural = 'Маршруты'
        verbose_name = 'Маршрут'


class Date(models.Model):
    id = models.UUIDField(primary_key=True, null=False, unique=True)
    minute = models.IntegerField(null=False, verbose_name='Минуты')
    hour = models.IntegerField(null=False, verbose_name='Часы')
    weekday = models.CharField(max_length=15, null=False, verbose_name='День недели')
    day = models.IntegerField(null=False, verbose_name='День месяца')
    month = models.IntegerField(null=False, verbose_name='Месяц')
    quarter = models.IntegerField(null=False, verbose_name='Квартал')
    year = models.IntegerField(null=False, verbose_name='Год')

    def __str__(self):
        return '{0}:{1} {2}.{3}.{4}'.format(self.hour, self.minute, self.day, self.month, self.year)

    class Meta:
        verbose_name_plural = 'Времена и даты'
        verbose_name = 'Время и дата'


class Voyage(models.Model):
    id = models.UUIDField(primary_key=True, null=False, unique=True)
    route = models.ForeignKey(Route, on_delete=models.PROTECT, null=False, verbose_name='Маршрут')
    mmsi = models.ForeignKey(Vessel, on_delete=models.PROTECT, null=False, verbose_name='MMSI')
    departure_date = models.ForeignKey(Date, on_delete=models.PROTECT, null=False, related_name='dep_date',
                                       verbose_name='Дата отправления')
    arrival_date = models.ForeignKey(Date, on_delete=models.PROTECT, null=False, related_name='arr_date',
                                     verbose_name='Дата прибытия')
    time_in_port = models.IntegerField(null=False, verbose_name='Время в порту')
    fuel_costs = models.IntegerField(null=False, verbose_name='Затраты на топливо')
    crew_costs = models.IntegerField(null=False, verbose_name='Затраты на экипаж')
    port_charges = models.IntegerField(null=False, verbose_name='Портовые расходы')
    insurance_costs = models.IntegerField(null=False, verbose_name='Затраты на страховку')
    total_costs = models.IntegerField(null=False, verbose_name='Сумма затрат')
    cargo_income = models.IntegerField(null=False, verbose_name='Доход от перевозки груза')
    net_total_freight = models.IntegerField(null=False, verbose_name='Чистый суммарный фрахт')
    voyage_profit = models.IntegerField(null=False, verbose_name='Прибыль за рейс')

    class Meta:
        verbose_name_plural = 'Рейсы'
        verbose_name = 'Рейс'
from django.db import models
from django.urls import reverse

class Station(models.Model):
    stationName = models.CharField('STATION_NAME', max_length=50, default='station_name')
    stationId = models.CharField('ID', max_length=50, unique=True)
    latitude = models.DecimalField('LAT', decimal_places=13, max_digits=17, null=True)
    longitude = models.DecimalField('LNT', decimal_places=13, max_digits=17, null=True)
    parkingBikeTotCnt = models.IntegerField('PARKED_BIKES', null=True)

    class Meta:
        ordering = ('stationName',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('community:station_detail', args=(self.pk,))
from django.db import models

# Create your models here.
class Bicy_stats(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    content = models.TextField('Content', null=True)
    period = models.DateTimeField('Period')

    class Meta:
        verbose_name = 'stat'
        verbose_name_plural = 'stats'
        ordering = ('-period',)

    def __str__(self):
        return self.title

class Station(models.Model):
    name = models.CharField('STATION_NAME', max_length=50)
    stationId = models.CharField('ID', max_length=50)
    latitude = models.DecimalField('LAT', decimal_places=13, max_digits=17)
    longitude = models.DecimalField('LNT', decimal_places=13, max_digits=17)
    parkingBikeTotCnt = models.IntegerField('PARKED_BIKES')

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


from django.db import models

class Station(models.Model):
    stationName = models.CharField('NAME', max_length=50)
    stationId = models.CharField('ID', max_length=50)

    def __str__(self):
        return self.stationName



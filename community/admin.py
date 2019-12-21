from django.contrib import admin
from .models import Station

@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ('stationName', 'stationId', 'parkingBikeTotCnt',)
    list_per_page = 100
    search_fields = ['stationName', 'stationId',]
from django.contrib import admin
from .models import Bicy_stats, Station

@admin.register(Bicy_stats)
class BicyStatsAdmin(admin.ModelAdmin):
    list_display = ('title', 'period')
    list_filter = ('period',)
    prepopulated_fields = {'description': ('title',)}

@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ('name', 'stationId', 'parkingBikeTotCnt')
    list_per_page = 10

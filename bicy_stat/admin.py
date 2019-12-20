from django.contrib import admin
from .models import Bicy_stats

@admin.register(Bicy_stats)
class BicyStatsAdmin(admin.ModelAdmin):
    list_display = ('title', 'period')
    list_filter = ('period',)
    prepopulated_fields = {'description': ('title',)}
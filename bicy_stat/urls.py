from django.urls import path
from .views import StatLV

app_name = 'bicy_stat'
urlpatterns = [
    path('', StatLV.as_view(), name='stats_index'),
]
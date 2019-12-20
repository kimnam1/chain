from django.urls import path
from .views import CommuLV, StationDV

app_name = 'community'
urlpatterns = [
    path('', CommuLV.as_view(), name='index'),
    path('<str:stationId>/', StationDV.as_view(), name='station_detail'),
]


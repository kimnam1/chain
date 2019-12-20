from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Station

class CommuLV(ListView):
    model = Station
    paginate_by = 10

class StationDV(DetailView):
    model = Station
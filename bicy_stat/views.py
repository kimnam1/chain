from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Bicy_stats

class StatLV(ListView):
    model = Bicy_stats
    template_name = "bicy_stat/stat_all.html"
    context_object_name = 'bicy_stats'
    paginate_by = 10



from django.views.generic import TemplateView, CreateView, ListView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from community.models import Station

#- Template View
class HomeView(TemplateView):
    template_name = "home.html"

class MyPageView(TemplateView):
    template_name = "mypage.html"

class OfficialSiteView(TemplateView):
    template_name = "official_site.html"

class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'

class FavoriteSV(ListView):
    model = Station
    template_name = 'favorite_station.html'
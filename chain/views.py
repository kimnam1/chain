from django.views.generic import TemplateView

#- Template View
class HomeView(TemplateView):
    template_name = "home.html"

class BicyStatView(TemplateView):
    template_name = ""
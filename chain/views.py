from django.views.generic import TemplateView

#- Template View
class HomeView(TemplateView):
    template_name = "home.html"

class MyPageView(TemplateView):
    template_name = "mypage.html"

class OfficialSiteView(TemplateView):
    template_name = "official_site.html"
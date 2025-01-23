
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'  # The name of the HTML file in templates folder to render.
class AboutPageView(TemplateView):
    template_name = 'about.html'
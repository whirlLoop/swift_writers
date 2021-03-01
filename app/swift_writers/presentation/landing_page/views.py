from django.views.generic import TemplateView


class LandingPageView(TemplateView):
    """Renders the home page
    """
    template_name = 'landing_page/index.html'

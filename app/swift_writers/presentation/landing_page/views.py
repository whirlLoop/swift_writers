from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin
from django.views.generic import FormView
from order.forms import OrderInitializationForm
from order.DAOs.essay_dao import EssayDAO
from order.DAOs.academic_level_dao import AcademicLevelDAO


class GetLandingPageView(TemplateView):
    """Renders the home page
    """
    template_name = 'landing_page/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OrderInitializationForm(
            EssayDAO().objects, AcademicLevelDAO().objects)
        return context


class PostLandingPageView(FormView):
    """Posts the Order form
    """
    template_name = 'landing_page/index.html'
    form_class = OrderInitializationForm(
        EssayDAO().objects, AcademicLevelDAO().objects)
    success_url = '/'

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class LandingPageView(View):
    """Posts and gets the landing page.
    """

    def get(self, request, *args, **kwargs):
        view = GetLandingPageView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PostLandingPageView.as_view()
        return view(request, *args, **kwargs)

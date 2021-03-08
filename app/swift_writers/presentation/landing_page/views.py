# from django.http import request
from django.views import View
from django.views.generic import TemplateView
from django.contrib import messages
from django.views.generic import FormView
from order.forms import OrderInitializationForm


class GetLandingPageView(TemplateView):
    """Renders the home page
    """
    template_name = 'landing_page/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OrderInitializationForm()
        return context


class PostLandingPageView(FormView):
    """Posts the Order form
    """
    template_name = 'landing_page/index.html'
    form_class = OrderInitializationForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        form.send_email(self.request)
        msg = (
            'Congratulations, we\'ve got your paper! We\'ve sent you a link '
            'in your email with the final steps. cheers.')
        messages.add_message(self.request, messages.SUCCESS, msg)
        return super().form_valid(form)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        msg = ('Please correct the errors in the form below')
        messages.add_message(self.request, messages.ERROR, msg)
        return response


class LandingPageView(View):
    """Posts and gets the landing page.
    """

    def get(self, request, *args, **kwargs):
        view = GetLandingPageView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PostLandingPageView.as_view()
        return view(request, *args, **kwargs)

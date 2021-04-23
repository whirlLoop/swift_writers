"""View for posting order
    """
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from order.forms import OrderForm


class PostOrderView(LoginRequiredMixin, FormView):

    form_class = OrderForm
    success_url = '/accounts/profile/'
    permission_denied_message = 'You need to be logged in place an order'
    template_name = 'registration/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_form'] = self.get_form()
        return context

    def form_valid(self, form):
        form.save(self.request)
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors.as_data())
        return super().form_invalid(form)

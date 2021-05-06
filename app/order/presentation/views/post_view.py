"""View for posting order
    """
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from order.forms import OrderForm
from order.context_processors import initial_order


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
        initial_order_context = initial_order(self.request)
        set_initial_order_data = initial_order_context.get('initial_order')
        set_initial_order_data.remove_data_from_session()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

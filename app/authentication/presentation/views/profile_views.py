from django.contrib import messages
from django.views.generic import UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from authentication.forms.change_form import AvatarUpdateForm
from order.forms import OrderForm
from order.context_processors import initial_order


class UserProfileView(LoginRequiredMixin, TemplateView):
    """Displays user profile and enables editing.
    """
    template_name = 'registration/profile.html'
    permission_denied_message = 'You need to be logged in to view your profile.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avatar_update_form'] = AvatarUpdateForm
        initial_order_context = initial_order(self.request)
        set_initial_order_data = initial_order_context.get(
            'initial_order').initial_order_data
        if set_initial_order_data:
            data = next(iter(set_initial_order_data.items()))[1]
            form = OrderForm()
            form.set_initial_data(data)
            context['order_form'] = form
            return context
        context['order_form'] = OrderForm
        return context


class AvatarUpdateView(LoginRequiredMixin, UpdateView):
    """Displays user profile and enables editing.
    """
    form_class = AvatarUpdateForm
    success_url = '/accounts/profile/'

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        msg = ('Your avatar has been changed successfully')
        messages.add_message(self.request, messages.SUCCESS, msg)
        return super().form_valid(form)

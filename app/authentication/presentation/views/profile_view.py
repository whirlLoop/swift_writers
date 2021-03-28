from django.views.generic import UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from authentication.forms.change_form import AvatarUpdateForm


class UserProfileView(LoginRequiredMixin, TemplateView):
    """Displays user profile and enables editing.
    """
    template_name = 'registration/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avatar_update_form'] = AvatarUpdateForm
        return context


class AvatarUpdateView(LoginRequiredMixin, UpdateView):
    """Displays user profile and enables editing.
    """
    template_name = 'registration/profile.html'
    form_class = AvatarUpdateForm
    success_url = '/accounts/profile/'

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

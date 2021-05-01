from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views.generic.edit import FormView
from order.forms import TempMaterialUploadForm
from authentication.forms.change_form import AvatarUpdateForm
from order.forms import OrderForm


class JsonableResponseMixin:
    """
    Mixin to add JSON support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """

    def form_invalid(self, form):
        is_ajax = self.request.META.get(
            'HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
        if is_ajax:
            return JsonResponse(form.errors, status=400)
        response = super().form_invalid(form)
        return response

    def form_valid(self, form):
        is_ajax = self.request.META.get(
            'HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
        material = form.save(self.request)
        if is_ajax:
            data = {
                'pk': material.pk,
                'filename': material.filename
            }
            return JsonResponse(data, status=201)
        form_data = {
            'pk': material.pk,
            'filename': material.filename
        }
        return self.render_to_response(
            self.get_context_data(
                data=form_data
            )
        )


class TempMaterialUploadView(LoginRequiredMixin, JsonableResponseMixin, FormView):

    form_class = TempMaterialUploadForm
    success_url = '/accounts/profile/'
    permission_denied_message = 'You need to be logged in upload materials.'
    template_name = 'registration/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['material_upload_form'] = self.get_form()
        context['avatar_update_form'] = AvatarUpdateForm
        context['order_form'] = OrderForm
        return context

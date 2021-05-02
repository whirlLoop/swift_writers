from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views.generic.edit import DeleteView
from django.http import HttpResponse
from order.models import TempOrderMaterial


class TempMaterialDeleteView(LoginRequiredMixin, DeleteView):

    success_url = '/accounts/profile/'
    permission_denied_message = 'You need to be logged in to delete materials.'
    template_name = 'registration/profile.html'
    model = TempOrderMaterial

    def delete(self, request, *args, **kwargs):
        self.get_object().delete()
        is_ajax = self.request.META.get(
            'HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
        if is_ajax:
            return JsonResponse(data={}, status=204, safe=False)
        return HttpResponse(status=204)

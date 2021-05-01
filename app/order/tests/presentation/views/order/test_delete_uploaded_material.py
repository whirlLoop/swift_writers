import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from common.tests.base_test import image
from order.tests.common.base_test import OrderBaseTestCase
from order.presentation.views import (
    TempMaterialDeleteView)
from authentication.forms.change_form import AvatarUpdateForm
from order.forms import OrderForm
from order.models import TempOrderMaterial


class DeleteTempFilesTestCase(OrderBaseTestCase):
    def setUp(self) -> None:
        super(DeleteTempFilesTestCase, self).setUp()
        self.form = {
            'material': image('test_avatar.jpeg')
        }

    def test_temp_material_delete_view_properties(self):
        self.assertTrue(issubclass(TempMaterialDeleteView, LoginRequiredMixin))
        self.assertTrue(issubclass(TempMaterialDeleteView, DeleteView))
        self.assertEqual(
            TempMaterialDeleteView.model, TempOrderMaterial)
        self.assertEqual(TempMaterialDeleteView.permission_denied_message,
                         'You need to be logged in to delete materials.')
        self.assertEqual(TempMaterialDeleteView.template_name,
                         'registration/profile.html')

    def test_can_delete_order_with_correct_details(self):
        response = self.client.post(
            '/order/material/', self.form, follow=True)
        self.assertEqual(response.status_code, 200)
        temp_material = [obj for obj in TempOrderMaterial.objects.all(
        ) if obj.filename == 'test_avatar.jpeg']
        temp_material = temp_material[0]
        self.assertEqual(
            response.context['data']['filename'],
            str(temp_material)
        )
        delete_response = self.client.post(
            '/order/material/temp/{}'.format(temp_material.pk), follow=True)
        self.assertEqual(delete_response.status_code, 204)
        deleted_material = TempOrderMaterial.objects.filter(
            pk=temp_material.pk)
        self.assertFalse(deleted_material)

    def test_ajax_request_successful(self):
        response = self.client.post(
            '/order/material/',
            self.form,
            follow=True,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest',
        )
        self.assertEqual(response.status_code, 201)
        response = json.loads(response.content)
        temp_material = [obj for obj in TempOrderMaterial.objects.all(
        ) if obj.filename == 'test_avatar.jpeg']
        temp_material = temp_material[0]
        delete_response = self.client.post(
            '/order/material/temp/{}'.format(temp_material.pk),
            follow=True,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest',
        )
        self.assertEqual(delete_response.status_code, 204)
        deleted_material = TempOrderMaterial.objects.filter(
            pk=temp_material.pk)
        self.assertFalse(deleted_material)

    def test_unsuccessful_ajax_request_returns_errors(self):
        response = self.client.post(
            '/order/material/temp/{}'.format(999),
            follow=True,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest',
        )
        self.assertEqual(response.status_code, 404)

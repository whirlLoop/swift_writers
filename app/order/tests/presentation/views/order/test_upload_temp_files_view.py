import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView
from common.tests.base_test import image
from order.tests.common.base_test import OrderBaseTestCase
from order.presentation.views import (
    TempMaterialUploadView)
from order.presentation.views.temp_material_upload_views import (
    JsonableResponseMixin)
from order.forms import TempMaterialUploadForm
from authentication.forms.change_form import AvatarUpdateForm
from order.forms import OrderForm
from order.models import TempOrderMaterial


class UploadTempFilesTestCase(OrderBaseTestCase):
    def setUp(self) -> None:
        super(UploadTempFilesTestCase, self).setUp()
        self.form = {
            'material': image('test_avatar.jpeg')
        }

    def test_temp_material_upload_view_properties(self):
        self.assertTrue(issubclass(TempMaterialUploadView, LoginRequiredMixin))
        self.assertTrue(issubclass(TempMaterialUploadView, FormView))
        self.assertTrue(issubclass(
            TempMaterialUploadView, JsonableResponseMixin))
        self.assertIsInstance(
            TempMaterialUploadView.form_class(), TempMaterialUploadForm)
        self.assertEqual(TempMaterialUploadView.permission_denied_message,
                         'You need to be logged in to upload materials.')
        self.assertEqual(TempMaterialUploadView.template_name,
                         'registration/profile.html')

    def test_can_post_order_with_correct_details(self):
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
        self.assertEqual(
            response.context['data']['pk'],
            temp_material.pk
        )

    def test_adds_required_objects_to_context(self):
        response = self.client.post(
            '/order/material/', self.form, follow=True)
        self.assertEqual(response.status_code, 200)
        temp_material = [obj for obj in TempOrderMaterial.objects.all(
        ) if obj.filename == 'test_avatar.jpeg']
        temp_material = temp_material[0]
        self.assertIsInstance(
            response.context['avatar_update_form'](),
            AvatarUpdateForm
        )
        self.assertIsInstance(
            response.context['order_form'](),
            OrderForm
        )

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
        self.assertEqual(
            response['filename'],
            str(temp_material)
        )
        self.assertEqual(
            response['pk'],
            temp_material.pk
        )

    def test_unsuccessful_ajax_request_returns_errors(self):
        response = self.client.post(
            '/order/material/',
            follow=True,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest',
        )
        self.assertEqual(response.status_code, 400)
        response = json.loads(response.content)
        self.assertEqual(
            response['material'][0],
            'This field is required.'
        )

from common.tests.base_test import image
from order.tests.common.base_test import OrderBaseTestCase
from order.forms import TempMaterialUploadForm
from order.models import TempOrderMaterial


class TempMaterialUploadFormTestCase(OrderBaseTestCase):

    def setUp(self):
        """setup test fixtures before using them"""
        super(TempMaterialUploadFormTestCase, self).setUp()
        self.form_data = {
            'client': self.logged_in_customer,
            'material': image('test_material.pdf')
        }
        self.form = TempMaterialUploadForm()

    def test_specifies_fields(self):
        fields = ['client', 'material']
        self.assertEqual(self.form.Meta.fields, fields)

    def test_specifies_model(self):
        self.assertIsInstance(self.form.Meta.model(), TempOrderMaterial)

    def validates_valid_form(self):
        TempMaterialUploadForm(self.form_data)
        self.assertTrue(self.form.is_valid())

    def test_saves_temp_material_appropriately(self):
        form = TempMaterialUploadForm(
            data={
                'client': self.form_data['client'],
            },
            files={'material': self.form_data['material']}
        )
        request = self.client.get("/")
        request.FILES = {}
        request.user = self.logged_in_customer
        self.assertTrue(form.is_valid())
        material = form.save(request)
        self.assertTrue(material)
        self.assertEqual(material.client, self.logged_in_customer)
        self.assertIn('test_material', material.filename)

    def test_checks_if_material_provided(self):
        self.form_data.pop('material')
        form = TempMaterialUploadForm(self.form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['material'][0],
                         'This field is required.')

    def test_restricts_file_to_50_mb(self):
        pass

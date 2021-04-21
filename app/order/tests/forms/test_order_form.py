from datetime import date
from order.tests.common.base_test import OrderBaseTestCase
from order.forms import OrderForm
from order.models import Order


class OrderFormTestCase(OrderBaseTestCase):

    def setUp(self) -> None:
        self.form = OrderForm()
        return super(OrderFormTestCase, self).setUp()

    def test_specifies_fields(self):
        fields = [
            'topic', 'type_of_paper',
            'no_of_pages', 'words', 'due_date', 'due_time',
            'academic_level', 'citation', 'discipline', 'description',
        ]
        self.assertEqual(self.form.Meta.fields, fields)

    def test_specifies_model(self):
        self.assertIsInstance(self.form.Meta.model(), Order)

    def test_topic_input_defines_a_placeholder(self):
        self.assertEqual(
            self.form.fields['topic'].widget.attrs['placeholder'],
            'Tell us the topic.'
        )

    def test_words_instead_input_defines_a_placeholder(self):
        self.assertEqual(
            self.form.fields['words'].widget.attrs['placeholder'],
            'Tell us the number of words instead.'
        )

    def test_due_date_field_has_correct_properties(self):
        due_date_input = self.form.fields['due_date']
        self.assertEqual(
            due_date_input.widget.attrs['min'], date.today()
        )
        self.assertEqual(
            due_date_input.widget.attrs['placeholder'], 'Select due date.'
        )

    def test_description_input_defines_a_placeholder(self):
        self.assertEqual(
            self.form.fields['description'].widget.attrs['placeholder'],
            'Describe what you need our writers to do. Add any other '
            'information you think might be useful'
        )

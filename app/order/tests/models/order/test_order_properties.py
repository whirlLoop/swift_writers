"""Test Order model properties."""
from django.db import models
from order.tests.common.base_test import OrderBaseTestCase
from order.models import Order
from authentication.models import User
from order.DAOs.essay_dao import EssayDAO
from order.DAOs.academic_level_dao import AcademicLevelDAO
from order.DAOs.discipline_dao import DisciplineDAO


class OrderModelPropertiesTestCase(OrderBaseTestCase):

    def setUp(self) -> None:
        super(OrderModelPropertiesTestCase, self).setUp()

    def test_model_sorts_orders_by_date(self):
        ordering = Order._meta.ordering
        self.assertEqual(ordering[0], 'date_created')

    def test_relation_on_delete_cascades(self):
        for f in self.order._meta.get_fields():
            if isinstance(f, models.ForeignKey):
                self.assertEquals(
                    f.remote_field.on_delete, models.SET_NULL,
                    '{} failed, value was {}'.format(
                        f.name, f.remote_field.on_delete
                    )
                )

    def test_order_relation_is_to_user_model(self):
        model = self.order._meta.get_field('client').related_model
        self.assertEqual(model, User)

    def test_defines_a_human_readable_name(self):
        self.assertEqual(
            str(self.order), 'Impact of social media on businesses'
        )

    def test_solution_foreign_key_related_name(self):
        for f in self.order._meta.get_fields():
            if isinstance(f, models.ForeignKey):
                self.assertEquals(
                    f.remote_field.related_name, 'orders',
                    '{} failed, value was {}'.format(
                        f.name, f.remote_field.on_delete
                    )
                )

    def test_topic_field_name(self):
        name = self.order._meta.get_field('topic').name
        self.assertEqual(name, 'topic')

    def test_topic_field_max_length(self):
        max_length = self.order._meta.get_field('topic').max_length
        self.assertEqual(max_length, 255)

    def test_topic_field_blank_false(self):
        blank = self.order._meta.get_field('topic').blank
        self.assertFalse(blank)

    def test_topic_field_defines_custom_required_error_message(self):
        messages = self.order._meta.get_field(
            'topic'
        ).error_messages
        topic_error_messages = {
            'required': (
                'Please tell us the topic for this assignment.'
            ),
        }
        self.assertDictContainsSubset(topic_error_messages, messages)

    def test_topic_is_an_index(self):
        index = self.order._meta.get_field('topic').db_index
        self.assertTrue(index)

    def test_topic_field_has_verbose_name(self):
        verbose_name = self.order._meta.get_field('topic').verbose_name
        self.assertEqual(verbose_name, 'Assignment Topic')

    def test_type_of_paper_field_name(self):
        name = self.order._meta.get_field('type_of_paper').name
        self.assertEqual(name, 'type_of_paper')

    def test_type_of_paper_field_defines_required_custom_error(self):
        messages = self.order._meta.get_field(
            'type_of_paper'
        ).error_messages
        type_of_paper_error_messages = {
            'required': (
                'Please tell us the type of paper.'
            ),
        }
        self.assertDictContainsSubset(type_of_paper_error_messages, messages)

    def test_type_of_paper_field_choices(self):
        essays = EssayDAO().objects
        EssayChoices = [
            (item.essay_name, item.essay_display_name)
            for item in essays
        ]
        model_choices = self.order._meta.get_field('type_of_paper').choices
        self.assertEqual(len(EssayChoices), len(model_choices))

    def test_type_of_paper_has_a_default_choice(self):
        default = self.order._meta.get_field('type_of_paper').default
        self.assertEqual(default, 'essay')

    def test_type_of_paper_field_max_length(self):
        max_len = self.order._meta.get_field('type_of_paper').max_length
        self.assertEqual(max_len, 80)

    def test_type_of_paper_field_has_verbose_name(self):
        verbose_name = self.order._meta.get_field('type_of_paper').verbose_name
        self.assertEqual(verbose_name, 'Type of paper')

    def test_no_of_pages_field_name(self):
        name = self.order._meta.get_field('no_of_pages').name
        self.assertEqual(name, 'no_of_pages')

    def test_no_of_pages_field_has_verbose_name(self):
        verbose_name = self.order._meta.get_field('no_of_pages').verbose_name
        self.assertEqual(verbose_name, 'Pages')

    def test_no_of_pages_field_has_default_value(self):
        default = self.order._meta.get_field('no_of_pages').default
        self.assertEqual(default, 1)

    def test_words_field_name(self):
        name = self.order._meta.get_field('words').name
        self.assertEqual(name, 'words')

    def test_words_field_verbose_name(self):
        name = self.order._meta.get_field('words').verbose_name
        self.assertEqual(name, 'Words')

    def test_words_field_blank_true(self):
        blank = self.order._meta.get_field('words').blank
        self.assertTrue(blank)

    def test_words_null_true(self):
        null = self.order._meta.get_field('words').null
        self.assertTrue(null)

    def test_due_date_field_name(self):
        name = self.order._meta.get_field('due_date').name
        self.assertEqual(name, 'due_date')

    def test_due_date_field_defines_required_custom_error(self):
        messages = self.order._meta.get_field(
            'due_date'
        ).error_messages
        due_date_error_messages = {
            'required': (
                'Please tell us when this paper should be complete.'
            ),
        }
        self.assertDictContainsSubset(due_date_error_messages, messages)

    def test_due_date_field_verbose_name(self):
        name = self.order._meta.get_field('due_date').verbose_name
        self.assertEqual(name, 'Due Date')

    def test_due_time_field_name(self):
        name = self.order._meta.get_field('due_time').name
        self.assertEqual(name, 'due_time')

    def test_due_time_field_choices(self):
        TIME_CHOICES = [
            ('0', '12 am (midnight)'), ('1', '1 am'), ('2', '2 am'),
            ('3', '3 am'), ('4', '4 am'), ('5', '5 am'), ('6', '6 am'),
            ('7', '7 am'), ('8', '8 am'), ('9', '9 am'), ('10', '10 am'),
            ('11', '11 am'), ('12', '12 pm (midnight)'), ('13', '1 pm'),
            ('14', '2 pm'), ('15', '3 pm'), ('16', '4 pm'), ('17', '5 pm'),
            ('18', '6 pm'), ('19', '7 pm'), ('20', '8 pm'), ('21', '9 pm'),
            ('22', '10 pm'), ('23', '11 pm'),
        ]
        field_choices = self.order._meta.get_field('due_time').choices
        self.assertEqual(field_choices, TIME_CHOICES)

    def test_due_time_field_default(self):
        default = self.order._meta.get_field('due_time').default
        self.assertEqual(default, '0')

    def test_due_time_field_max_length(self):
        max_length = self.order._meta.get_field('due_time').max_length
        self.assertEqual(max_length, 2)

    def test_academic_level_field_name(self):
        name = self.order._meta.get_field('academic_level').name
        self.assertEqual(name, 'academic_level')

    def test_academic_level_field_defines_required_custom_error(self):
        messages = self.order._meta.get_field(
            'academic_level'
        ).error_messages
        academic_level_error_messages = {
            'required': (
                'Please tell us your academic level.'
            ),
        }
        self.assertDictContainsSubset(academic_level_error_messages, messages)

    def test_academic_level_field_choices(self):
        academic_levels = AcademicLevelDAO().objects
        AcademicLevelChoices = [
            (item.academic_level_name, item.academic_level_display_name)
            for item in academic_levels
        ]
        model_choices = self.order._meta.get_field('academic_level').choices
        self.assertEqual(len(AcademicLevelChoices), len(model_choices))

    def test_academic_level_has_a_default_choice(self):
        default = self.order._meta.get_field('academic_level').default
        self.assertEqual(default, 'college')

    def test_academic_level_field_max_len(self):
        max_len = self.order._meta.get_field('academic_level').max_length
        self.assertEqual(max_len, 80)

    def test_academic_level_field_has_verbose_name(self):
        verbose_name = self.order._meta.get_field(
            'academic_level').verbose_name
        self.assertEqual(verbose_name, 'Academic Level')

    def test_citation_field_name(self):
        name = self.order._meta.get_field('citation').name
        self.assertEqual(name, 'citation')

    def test_citation_field_defines_required_custom_error(self):
        messages = self.order._meta.get_field(
            'citation'
        ).error_messages
        citation_error_messages = {
            'required': (
                'Please select the referencing style for your paper.'
            ),
        }
        self.assertDictContainsSubset(citation_error_messages, messages)

    def test_citation_has_a_default_choice(self):
        default = self.order._meta.get_field('citation').default
        self.assertEqual(default, 'APA 6')

    def test_citation_field_max_len(self):
        max_len = self.order._meta.get_field('citation').max_length
        self.assertEqual(max_len, 255)

    def test_citation_field_has_verbose_name(self):
        verbose_name = self.order._meta.get_field(
            'citation').verbose_name
        self.assertEqual(verbose_name, 'Format / Citation')

    def test_discipline_field_name(self):
        name = self.order._meta.get_field('discipline').name
        self.assertEqual(name, 'discipline')

    def test_discipline_field_defines_required_custom_error(self):
        messages = self.order._meta.get_field(
            'discipline'
        ).error_messages
        discipline_error_messages = {
            'required': (
                'Please tell us your discipline.'
            ),
        }
        self.assertDictContainsSubset(discipline_error_messages, messages)

    def test_discipline_field_choices(self):
        disciplines = DisciplineDAO().objects
        DisciplineChoices = [
            (item.discipline_id, item.discipline_name)
            for item in disciplines
        ]
        model_choices = self.order._meta.get_field('discipline').choices
        self.assertEqual(len(DisciplineChoices), len(model_choices))

    def test_discipline_field_max_len(self):
        max_len = self.order._meta.get_field('discipline').max_length
        self.assertEqual(max_len, 255)

    def test_discipline_field_has_verbose_name(self):
        verbose_name = self.order._meta.get_field(
            'discipline').verbose_name
        self.assertEqual(verbose_name, 'Discipline')

    def test_discipline_field_has_a_default(self):
        default = self.order._meta.get_field('discipline').default
        self.assertEqual(default, 1)

    def test_description_field_name(self):
        name = self.order._meta.get_field('description').name
        self.assertEqual(name, 'description')

    def test_description_field_null_true(self):
        null = self.order._meta.get_field('description').null
        self.assertTrue(null)

    def test_description_field_blank_true(self):
        blank = self.order._meta.get_field('description').blank
        self.assertTrue(blank)

    def test_status_field_name(self):
        name = self.order._meta.get_field('status').name
        self.assertEqual(name, 'status')

    def test_status_field_choices(self):
        STATUS_CHOICES = [
            ('placed', 'PLACED'), ('confirmed', 'CONFIRMED'),
            ('healthy', 'HEALTHY'), ('unhealthy', 'UNHEALTHY'),
            ('dangerous', 'DANGEROUS'), ('critical', 'CRITICAL'),
            ('indeterminate', 'INDETERMINATE'), ('cancelled', 'CANCELLED'),
            ('delivered', 'DELIVERED'), ('finished', 'FINISHED')
        ]
        choices = self.order._meta.get_field('status').choices
        self.assertEqual(choices, STATUS_CHOICES)

    def test_status_field_max_length(self):
        max_length = self.order._meta.get_field('status').max_length
        self.assertEqual(max_length, 40)

    def test_status_field_error_messages(self):
        messages = self.order._meta.get_field(
            'status'
        ).error_messages
        status_error_messages = {
            'required': (
                'Please provide the status for this order.'
            ),
        }
        self.assertDictContainsSubset(status_error_messages, messages)

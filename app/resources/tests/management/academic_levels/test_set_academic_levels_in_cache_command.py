from io import StringIO
import json
from django.core.management import call_command, get_commands
from resources.management.commands.set_academic_levels_cache import Command
from resources.tests.common.base_test_case import BaseTestCase


class SetEssayAcademicLevelsTest(BaseTestCase):

    def setUp(self):
        super(SetEssayAcademicLevelsTest, self).setUp()

    def test_class_instantiation(self):
        command_help_message = (
            "Fetches academic_levels from external api and sets them "
            "in the cache as an academic_levels bytes object that can "
            "be converted into a list of academic levels objects/dicts"
        )
        success_message = ("Wohoo! academic_levels successfully cached.")
        self.assertEqual(Command.help, command_help_message)
        self.assertEqual(Command.success_message, success_message)

    def test_command_in_command_list(self):
        self.assertIn('set_academic_levels_cache', get_commands())

    def test_fetched_academic_levels_set_in_cache(self):
        self.cache.delete('academic_levels')
        Command().handle()
        self.assertIsInstance(json.loads(
            self.cache.get("academic_levels")), list)
        self.assertIsInstance(json.loads(
            self.cache.get("academic_levels"))[0], dict)

    def test_successful_std_output_printed(self):
        out = StringIO()
        call_command('set_academic_levels_cache', stdout=out)
        self.assertIn(Command.success_message, out.getvalue())

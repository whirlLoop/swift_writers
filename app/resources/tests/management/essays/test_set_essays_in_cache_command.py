from io import StringIO
import json
from django.core.management import call_command, get_commands
from django.core.management.base import CommandError
from resources.management.commands.set_essays_cache import Command
from resources.tests.common.base_test_case import BaseTestCase


class SetEssayCacheTest(BaseTestCase):

    def setUp(self):
        super(SetEssayCacheTest, self).setUp()

    def test_class_instantiation(self):
        command_help_message = (
            "Fetches essays from external api and sets them in the cache "
            "as an essays bytes object that can be converted into a list "
            "of essay objects/dicts"
        )
        success_message = ("Wohoo! essays successfully cached.")
        self.assertEqual(Command.help, command_help_message)
        self.assertEqual(Command.success_message, success_message)

    def test_command_in_command_list(self):
        self.assertIn('set_essays_cache', get_commands())

    def test_fetched_essays_set_in_cache(self):
        self.cache.delete('essays')
        Command().handle()
        self.assertIsInstance(json.loads(self.cache.get("essays")), list)
        self.assertIsInstance(json.loads(self.cache.get("essays"))[0], dict)

    def test_successful_std_output_printed(self):
        out = StringIO()
        call_command('set_essays_cache', stdout=out)
        self.assertIn(Command.success_message, out.getvalue())

    def test_raises_command_error(self):
        self.cache.delete('academic_levels')
        with self.assertRaises(CommandError):
            with self.settings(BASE_ESSAYS_URL=''):
                Command().handle()

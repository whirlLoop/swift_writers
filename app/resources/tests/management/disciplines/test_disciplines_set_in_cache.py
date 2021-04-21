from io import StringIO
import json
import pytest
from django.core.management import call_command, get_commands
from django.core.management.base import CommandError
from resources.management.commands.set_disciplines_cache import Command
from resources.tests.common.base_test_case import BaseTestCase


class SetEssayCacheTest(BaseTestCase):

    def setUp(self):
        super(SetEssayCacheTest, self).setUp()

    def test_class_instantiation(self):
        command_help_message = (
            "Fetches disciplines from external api and sets them in the cache "
            "as an disciplines bytes object that can be converted into a list "
            "of essay objects/dicts"
        )
        success_message = ("Wohoo! disciplines successfully cached.")
        self.assertEqual(Command.help, command_help_message)
        self.assertEqual(Command.success_message, success_message)

    def test_command_in_command_list(self):
        self.assertIn('set_disciplines_cache', get_commands())

    def test_fetched_disciplines_set_in_cache(self):
        self.cache.delete('disciplines')
        with pytest.raises(Exception):
            Command().handle()
            self.assertIsInstance(json.loads(self.cache.get("disciplines")), list)
            self.assertIsInstance(json.loads(
                self.cache.get("disciplines"))[0], dict)

    def test_successful_std_output_printed(self):
        out = StringIO()
        with pytest.raises(Exception):
            call_command('set_disciplines_cache', stdout=out)
            self.assertIn(Command.success_message, out.getvalue())

    def test_raises_command_error(self):
        self.cache.delete('essays')
        with self.assertRaises(CommandError):
            with self.settings(BASE_DISCIPLINES_URL=''):
                Command().handle()

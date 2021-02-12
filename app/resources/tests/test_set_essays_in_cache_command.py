from io import StringIO
import json
from unittest.mock import patch
from django.core.management import call_command, get_commands
from django.test import TestCase
from django_redis import get_redis_connection
from resources.management.commands.set_essays_cache import Command


class SetEssayCacheTest(TestCase):

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
        cache = get_redis_connection()
        cache.delete('essays')
        Command().handle()
        self.assertIsInstance(json.loads(cache.get("essays")), list)
        self.assertIsInstance(json.loads(cache.get("essays"))[0], dict)

    def test_successful_std_output_printed(self):
        out = StringIO()
        call_command('set_essays_cache', stdout=out)
        self.assertIn(Command.success_message, out.getvalue())

    def tearDown(self):
        get_redis_connection("default").flushall()

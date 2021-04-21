"""
Contains a command which when executed, fetches Disciplines data from an
external api, and sets it in the cache
"""
from django.core.management.base import BaseCommand, CommandError
from resources.utils import FetchDisciplines


class Command(BaseCommand):
    """
    A command that fetches and sets the data.
    """

    help = (
        "Fetches disciplines from external api and sets them in the cache "
        "as an disciplines bytes object that can be converted into a list "
        "of essay objects/dicts"
    )

    success_message = ("Wohoo! disciplines successfully cached.")

    def handle(self, *args, **options):
        try:
            FetchDisciplines().fetch_all()
            self.stdout.write(self.style.SUCCESS(self.success_message))
        except Exception:
            raise CommandError()

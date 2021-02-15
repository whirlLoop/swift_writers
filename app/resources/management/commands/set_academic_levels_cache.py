"""
Contains a command which when executed, fetches academic levels data from
an external api, and sets it in the cache
"""
from django.core.management.base import BaseCommand, CommandError
from resources.utils import FetchAcademicLevels


class Command(BaseCommand):
    """
    A command that fetches and sets the data.
    """

    help = (
        "Fetches academic_levels from external api and sets them "
        "in the cache as an academic_levels bytes object that can "
        "be converted into a list of academic levels objects/dicts"
    )

    success_message = ("Wohoo! academic_levels successfully cached.")

    def handle(self, *args, **options):
        try:
            FetchAcademicLevels().fetch_all()
            self.stdout.write(self.style.SUCCESS(self.success_message))
        except Exception:
            raise CommandError()

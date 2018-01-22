from django.core.management.base import BaseCommand
from api.models import Site

class Command(BaseCommand):
    help = 'Dump data'

    def handle(self, *args, **options):
        Site.populate()
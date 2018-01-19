from django.core.management.base import BaseCommand, CommandError
from api.models import Data

class Command(BaseCommand):
    help = 'Dump data'

    def handle(self, *args, **options):
        Data.update()
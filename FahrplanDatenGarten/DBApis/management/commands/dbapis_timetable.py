# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError
from DBApis.hafasImport import HafasImport
from core.models import Stop

class Command(BaseCommand):
    help = 'Imports the Timetable from DB API'

    def add_arguments(self, parser):
        parser.add_argument('stopname', nargs='?', type=str)

    def handle(self, *args, **options):
        stop = Stop.objects.filter(stopname__name=options['stopname']).first()
        hafasimport = HafasImport()
        hafasimport.import_timetable(stop)

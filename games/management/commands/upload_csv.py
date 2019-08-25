import os
import csv

from django.core.management.base import BaseCommand
from django.conf import settings

from games.models import Game
from games.serializers import GameSerializer


class Command(BaseCommand):
    """Uploads games csv into the database"""

    def add_arguments(self, parser):
        parser.add_argument('file', type=str, help='Name of the file to be uploaded.')

    def handle(self, *args, **kwargs):
        file_name = kwargs['file']
        file_path = os.path.join(getattr(settings, "GAMES_CSV_PATH"), file_name)
        cnt = 0
        with open(file_path, 'r') as file:
            for row in csv.DictReader(file):
                if not row['genre'].strip():
                    row['genre'] = 'null'
                serialized_data = GameSerializer(data=row)
                if serialized_data.is_valid():
                    # save if the data has no errors
                    serialized_data.save()
                    cnt += 1
                else:
                    raise ValueError("File contains invalid record.")
        self.stdout.write(f"Successfully uploaded {cnt} records from {file_name}.")

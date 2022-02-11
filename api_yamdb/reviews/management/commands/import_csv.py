import csv
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from tqdm import tqdm

from ._csv_data_relations import csv_data_relation


class Command(BaseCommand):
    help = 'Imports csv data from files in staic/data/ into database'

    def handle(self, *args, **kwargs):
        objects = self._create_list_of_model_objects(csv_data_relation)
        for obj_list in objects:
            table_name = type(obj_list[0]).__name__
            self.stdout.write(f'\nSaving data to table "{table_name}":')
            for obj in tqdm(obj_list):
                obj.save()

    def _create_model_objects_from_csv_data(self, csv_file, model):
        """Returns list of model objects, populated from csv_file data."""
        model_objects = []
        with open(csv_file, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                model_object = model(**row)
                model_objects.append(model_object)
        return model_objects

    def _create_list_of_model_objects(self, csv_data_relation):
        """Create a list of model object lists."""
        model_objects_list = []
        csv_dir = Path(settings.BASE_DIR) / 'static' / 'data'
        for csv_pair in csv_data_relation:
            csv_file = csv_dir / csv_pair['filename']
            model = csv_pair['model']
            if not csv_file.exists():
                raise CommandError(
                    f'File {csv_file} not found!'
                )
            model_objects = self._create_model_objects_from_csv_data(
                csv_file,
                model
            )
            model_objects_list.append(model_objects)
        return model_objects_list

import os.path
from django.core.management.base import BaseCommand
from apps.imdb.models import Person


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("-f", "--file", type=str, required=True)

    def handle(self, *args, **options):
        print("Starting transfer. Please wait ...")
        file = options.get("file")

        if not os.path.exists(file):
            print("No such file.")

        with open(file, encoding="utf-8") as f:
            for line in f.readlines():
                if (not line) or(not line.startswith("nm")):
                    continue
                data = line.split("\t")
                birth_date = data[2]
                death_date = data[3]
                person_data = {
                    'name': data[1],
                    'birth_year': None if data[2] == "\\N" else f"{data[2]}-01-01",
                    'death_year': None if data[3] == "\\N" else f"{data[3]}-01-01",
                }
                person, created = Person.objects.get_or_create(
                    imdb_id=data[0], defaults=person_data
                )

                if created:
                    Person.objects.filter(id=person.id).update(**person_data)

        print('Data transfer complete')

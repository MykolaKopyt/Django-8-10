import json
import os.path
from django.core.management.base import BaseCommand
from apps.imdb.models import Person, Movie, PersonMovie


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
                if (not line) or(not line.startswith("tt")):
                    continue
                data = line.split("\t")
                person = Person.objects.filter(imdb_id=data[2]).first()
                if not person:
                    continue
                movie = Movie.objects.filter(imdb_id=data[0]).first()
                if not movie:
                    continue
                pm_data = {
                    "order": int(data[1]),
                    "category": None if data[3] == "\\N" else data[3],
                    "job": None if data[4] == "\\N" else data[4],
                    "characters": None if data[5].startswith("\\N") else json.loads(data[5])
                }
                pm, created = PersonMovie.objects.get_or_create(
                    movie_id=movie,
                    person_id=person,
                    defaults=pm_data
                )
                if created:
                    PersonMovie.objects.filter(id=pm.id).update(**pm_data)

        print('Data transfer complete')

import os.path
from django.core.management.base import BaseCommand
from apps.imdb.models import Movie


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
                if (not line) or (not line.startswith("tt")):
                    continue
                data = line.split("\t")
                if data[1] not in ("movie", "short"):
                    continue
                movie_data = {
                    "title_type": data[1],
                    "name": data[2],
                    "is_adult": data[4],
                    "year": None if data[5] == "\\N" else int(data[5]),
                    "genres": None if data[8].startswith("\\N") else data[8].split(","),
                }
                movie, created = Movie.objects.get_or_create(
                    imdb_id=data[0], defaults=movie_data
                )

                if created:
                    Movie.objects.filter(id=movie.id).update(**movie_data)

        print('Data transfer complete')

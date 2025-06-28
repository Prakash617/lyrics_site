from django.core.management.base import BaseCommand
from music.models import Artist, Song, Genre, Tag
from django.utils.text import slugify

class Command(BaseCommand):
    help = "Seed the database with Nepali lyrics and song metadata"

    def handle(self, *args, **kwargs):
        # Create or get Artists
        sugam = Artist.objects.get_or_create(name="Sugam Pokharel")[0]
        neetesh = Artist.objects.get_or_create(name="Neetesh Jung Kunwar")[0]

        # Create or get Genre
        pop = Genre.objects.get_or_create(name="Pop")[0]
        alt = Genre.objects.get_or_create(name="Alternative")[0]

        # Create or get Tags
        romantic = Tag.objects.get_or_create(name="romantic")[0]
        emotional = Tag.objects.get_or_create(name="emotional")[0]

        # Song data list
        songs_data = [
            {
                "title": "Kati Din Bitey",
                "artists": [sugam],
                "lyrics": """[Am]Kati din bitey [G]timi sanga bolna sakina\n[F]Mero man bhitra [C]kehi kura chha timilai bhanna""",
                "youtube_link": "https://www.youtube.com/watch?v=dummy1",
                "category": "classic",
                "genre": pop,
                "tags": [romantic],
                "language": "ne",
                "album": "Sugam Hits",
                "release_year": 2005,
            },
            {
                "title": "Flirty Maya",
                "artists": [neetesh],
                "lyrics": """[C]Flirty maya, timi [G]mero maya\n[Am]Mutu choli [F]jane maya""",
                "youtube_link": "https://www.youtube.com/watch?v=dummy2",
                "category": "trending",
                "genre": alt,
                "tags": [emotional, romantic],
                "language": "ne",
                "album": "Neetesh Vibes",
                "release_year": 2018,
            },
        ]

        for data in songs_data:
            slug = slugify(f"{data['title']}-{data['release_year']}")
            song, created = Song.objects.get_or_create(
                slug=slug,
                defaults={
                    "title": data["title"],
                    "lyrics": data["lyrics"],
                    "youtube_link": data["youtube_link"],
                    "category": data["category"],
                    "genre": data["genre"],
                    "language": data["language"],
                    "album": data["album"],
                    "release_year": data["release_year"],
                }
            )
            song.artists.set(data["artists"])
            song.tags.set(data["tags"])
            song.save()

        self.stdout.write(self.style.SUCCESS("✅ Nepali songs seeded successfully."))

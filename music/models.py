from django.db import models
from django.utils.text import slugify

class Artist(models.Model):
    name = models.CharField(max_length=100, unique=True)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='artists/', blank=True, null=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Song(models.Model):
    CATEGORY_CHOICES = [
        ('trending', 'Trending'),
        ('classic', 'Classic'),
        ('recent', 'Recent'),
    ]

    LANGUAGE_CHOICES = [
        ('en', 'English'),
        ('ne', 'Nepali'),
        ('hi', 'Hindi'),
        # Add more if needed
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    artists = models.ManyToManyField(Artist, related_name='songs')
    lyrics = models.TextField(help_text="Include chords inline like: [C]Hello [G]world")
    youtube_link = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, default='en')
    album = models.CharField(max_length=100, blank=True)
    release_year = models.PositiveIntegerField(blank=True, null=True)
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)
    view_count = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.title}-{self.release_year or ''}")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

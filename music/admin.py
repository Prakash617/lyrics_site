from django.contrib import admin
from .models import Artist, Song, Genre, Tag

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_artists', 'release_year', 'category', 'language')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'lyrics', 'album']
    list_filter = ['category', 'language', 'release_year']
    filter_horizontal = ['artists', 'tags']

    def get_artists(self, obj):
        return ", ".join([artist.name for artist in obj.artists.all()])
    get_artists.short_description = 'Artists'

admin.site.register(Artist)
admin.site.register(Genre)
admin.site.register(Tag)

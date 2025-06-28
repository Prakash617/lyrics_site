from django.shortcuts import render
from .models import *
from django.shortcuts import render, get_object_or_404

# Create your views here.

def index(request):
    trending_songs = Song.objects.filter(category='trending')[:6]
    artists = Artist.objects.all()[:4]
    genres = Genre.objects.all()

    return render(request, 'music/index.html', {
        'trending_songs': trending_songs,
        'artists': artists,
        'genres': genres
    })


def song_detail(request, slug):
    song = get_object_or_404(Song, slug=slug)
    return render(request, 'music/song_detail.html', {'song': song})

from django.shortcuts import render
from .models import Song

def song_list(request):
    query = request.GET.get('q', '')
    songs = Song.objects.filter(title__icontains=query) if query else Song.objects.all()
    return render(request, 'music/song_list.html', {'songs': songs})

from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = "index"),
    path('song_list', views.song_list, name='song_list'),
        path('songs/<slug:slug>/', views.song_detail, name='song_detail'),  # ✅ this is required
]
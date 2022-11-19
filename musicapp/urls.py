from django.urls import path
from .views import SongList, ArtistList, SongDetail

urlpatterns = [
    path("songs/", SongList.as_view()),
    path("songs/<int:pk>/", SongDetail.as_view()),
    path("artists/", ArtistList.as_view())
]
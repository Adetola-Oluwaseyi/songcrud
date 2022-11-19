from django.shortcuts import render
from .models import Song, Artiste, Lyric
from .serializers import SongSerializer, ArtisteSerializer, LyricSerializer

from rest_framework import generics


class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class ArtistList(generics.ListCreateAPIView):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer
class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
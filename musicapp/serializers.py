from rest_framework import serializers
from .models import Artiste, Lyric, Song

class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = ["first_name", "last_name", "age"] #list the fields you wanna serialize

class LyricSerializer (serializers.ModelSerializer):
    class Meta:
        model = Lyric
        fields = ["content", "song_id"] #list the fields you wanna serialize

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ["title", "date_released", "likes", "artiste_id"] #list the fields you wanna serialize

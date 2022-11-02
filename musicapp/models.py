from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length= 40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name
class Song(models.Model):
    title = models.CharField(max_length= 100)
    date_released = models.DateField()
    likes = models.IntegerField()
    artiste_id = models.ForeignKey(Artiste, on_delete = models.PROTECT)

    def __str__(self):
        return self.title
class Lyric(models.Model):
    content = models.IntegerField()
    song_id = models.ForeignKey(Song, on_delete = models.PROTECT)

    def __str__(self):
        return self.content
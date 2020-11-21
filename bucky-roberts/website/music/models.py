from django.db import models
from django.urls import reverse


# Create your models here.


class Album(models.Model):
        artist = models.CharField(max_length=50)
        artist_logo = models.FileField(upload_to='artist_cover')
        album_title = models.CharField(max_length=300)
        genre = models.CharField(max_length=100)
        album_logo = models.FileField(upload_to='album_cover')

        # whenever we create a new album, it will redirect to this URL.
        def get_absolute_url(self):
                return reverse('music:detail', kwargs={'pk': self.pk})

        def __str__(self):
                return self.album_title + ' - ' + self.artist


class song(models.Model):
        album = models.ForeignKey(Album, on_delete=models.CASCADE)
        file_type = models.CharField(max_length=10)
        song_title = models.CharField(max_length=250)
        is_fav = models.BooleanField(default=False)

        def __str__(self):
                return self.song_title
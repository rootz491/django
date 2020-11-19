from django.db import models
from django.urls import reverse


# Create your models here.


class Album(models.Model):
        artist = models.CharField(max_length=50)
        artist_logo = models.URLField(max_length=500, default="https://images.unsplash.com/photo-1486092642310-0c4e84309adb?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80")
        album_title = models.CharField(max_length=300)
        genre = models.CharField(max_length=100)
        album_logo = models.URLField(max_length=1000, default="https://images.unsplash.com/photo-1559713044-c7329e177eb0?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=667&q=80")

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

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Album, song




class IndexView(generic.ListView):
        template_name = 'music/index.html'
        context_object_name = 'albums'

        def get_queryset(self):
                # get all album as an object
                return Album.objects.all()


class DetailView(generic.DetailView):
        model = Album
        template_name = 'music/detail.html'
        context_object_name = 'albumObj'


class AlbumCreate(CreateView):
        model = Album
        template_name = 'music/album_form.html'
        fields = ['artist', 'album_title', 'genre', 'album_logo', 'artist_logo']




def favourite(request, album_id):
        album = get_object_or_404(Album, pk=album_id)
        try:
                selected_song = album.song_set.get(pk=request.POST['song'])
        except (KeyError, selected_song.doesNotExist):
                return render(request, 'music/detail.html', {
                        'album': album,
                        'error_message': 'you did not select a valid song!'
                })
        else:
                selected_song.is_fav = not selected_song.is_fav
                selected_song.save()
        return HttpResponseRedirect(reverse('music:detail', args=(album_id,)))       # redirect to same page.

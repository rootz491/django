from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
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
        fields = ['artist', 'album_title', 'genre', 'album_logo', 'artist_logo']


class AlbumUpdate(UpdateView):
        model = Album
        fields = ['artist', 'album_title', 'genre', 'album_logo', 'artist_logo']


class AlbumDelete(DeleteView):
        model = Album
        success_url = reverse_lazy('music:index')





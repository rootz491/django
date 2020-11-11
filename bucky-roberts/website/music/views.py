from .models import Album                       # get data from models (indirectly from database)

# from django.http import HttpResponse          # used it for rendering using METHOD 1
# from django.template import loader            # to load the templates for METHOD 1

from django.shortcuts import render             # to render template / send back response. METHOD 2
from django.shortcuts import get_object_or_404  # shortcut for try catch block.
from django.http import Http404                 # Http404 for returning 404 if page not found






# Create your views here.

#       METHOD 1

# def index(request):
#         all_albums = Album.objects.all()
#         template = loader.get_template('music/index.html')
#         context = {
#                 'all_albums': all_albums,
#         }
#         return HttpResponse(template.render(context, request))
#         # return HttpResponse('<h1>hello music</h1>')


#       METHOD 2 [USE THIS]

def index(request):
        albums = Album.objects.all()
        return render(request, 'music/index.html', {'albums': albums, })





#       again METHOD 1

# def detail(request, album_id):
#         album = Album.objects.get(pk=album_id)
#         print(album.album_title)
#         template = loader.get_template('music/detail.html')
#         context = {
#                 "albumObj": album,
#         }
#         return HttpResponse(template.render(context, request))
#         # return HttpResponse('<h1>' + album.album_title + '</h1>')


#       METHOD 2 [using this]

# def detail(request, album_id):
#         try:                                                                                    # check data is present the user want to retrieve or not.
#                 album = Album.objects.get(pk=album_id)                                          # get data from database.
#         except Album.DoesNotExist:                                                              # if not then
#                 raise Http404("Album not Found! maybe it is deleted or it never existed.")      # raise an HTTP 404 means data not exists.
#         return render(request, 'music/detail.html', {"albumObj": album})                        # render the page


#       METHOD 2 - Shortcut for Try Catch block.

def detail(request, album_id):
        # try:                                                                                    # check data is present the user want to retrieve or not.
        #         album = Album.objects.get(pk=album_id)                                          # get data from database.
        # except Album.DoesNotExist:                                                              # if not then
        #         raise Http404("Album not Found! maybe it is deleted or it never existed.")      # raise an HTTP 404 means data not exists.
        album = get_object_or_404(Album, pk=album_id)
        return render(request, 'music/detail.html', {"albumObj": album})                        # render the page


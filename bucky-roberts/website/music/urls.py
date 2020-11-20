from django.urls import path
from . import views

# namespacing
app_name = 'music'

#       OLD METHOD [non-generic]
# urlpatterns = [
#         path(r'', views.index, name='index'),                           # /music
#         path(r'album=<int:album_id>/', views.detail, name='detail'),    # /music/album=1/
#         path(r'album=<int:album_id>/favourite/', views.favourite, name='favourite')
# ]


#       GENERIC VIEWS

urlpatterns = [
        path(r'', views.IndexView.as_view(), name='index'),
        path(r'album=<int:pk>/', views.DetailView.as_view(), name='detail'),
        path(r'album=<int:album_id>/favourite/', views.favourite, name='favourite'),
        path(r'album/add/', views.AlbumCreate.as_view(), name='album-add'),
        path(r'album=<int:pk>/update/', views.AlbumUpdate.as_view(), name='album-update'),
        path(r'album=<int:pk>/delete/', views.AlbumDelete.as_view(), name='album-delete'),
]

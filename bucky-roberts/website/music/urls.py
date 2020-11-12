from django.urls import path
from . import views

# namespacing
app_name = 'music'

urlpatterns = [
        path(r'', views.index, name='index'),                           # /music
        path(r'album=<int:album_id>/', views.detail, name='detail'),    # /music/album=1/
        path(r'album=<int:album_id>/favourite/', views.favourite, name='favourite')
]

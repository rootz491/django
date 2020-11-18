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
]

from django.urls import path
from . import views

urlpatterns = [
        path(r'', views.index, name='index'),
        path(r'<int:album_id>/', views.detail, name='detail'),
]

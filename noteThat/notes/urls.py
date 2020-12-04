from django.urls import path
from .views import *


app_name = 'note'

urlpatterns = [
        path(r'', index, name='index'),
        path(r'search/', search, name='search'),
        path(r'bookmarked/', bookmarked, name='bookmarked'),
        path(r'<str:id>/bookmark/', bookmark, name='bookmark'),
        path(r'create/', create, name='create'),
        path(r'<str:id>/delete/', delete, name='delete'),
        path(r'<str:id>/edit/', edit, name='edit'),
        path(r'user/logout/', logoutUser, name='logout'),
        path(r'user/login/', loginUser, name='login'),
        path(r'user/register/', register, name='register'),
        path(r'landing/', landing, name='landing')
]

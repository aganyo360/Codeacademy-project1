from django.urls import path
from . import views
urlpatterns= [
    path('', views.index, name='index'),
    path('movie_detail', views.movie_detail, name='movie_detail'),
    path('genre_detail', views.genre_detail, name ='genre_detail')
]
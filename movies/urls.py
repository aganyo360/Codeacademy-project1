from django.urls import path
from . import views
urlpatterns= [
    path('', views.index, name='movies_index'),
    path('<int:movie_id>', views.detail, name='movies_detail'),
    path('movie_detail', views.movie_detail, name='movie_detail'),
    path('genre_detail', views.genre_detail, name ='genre_detail')
]
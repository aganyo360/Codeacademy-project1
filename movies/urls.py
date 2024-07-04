from django.urls import path
from . import views
app_name = 'movies'
urlpatterns= [
    path('', views.index, name='movies_index'),
    path('<int:movie_id>', views.detail, name='detail'),
    path('genre_detail', views.genre_detail, name ='genre_detail')
]
from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie, Genre
# Create your views here.
def index(request):
    movies = Movie.objects.all()
    output = ', '.join([m.title for m in movies])
    return HttpResponse(output)

def movie_detail(request):
    movies = Movie.objects.get(id=2)
    # context = 
    return HttpResponse(movies)

def genre_detail(request):
    genres = (Genre.objects.all())
    output = '    \n' .join([g.name for g in genres])
    return HttpResponse(output)
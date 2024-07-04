from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie, Genre
# Create your views here.
def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies':movies})
def detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'movies/detail.html', {'movie':movie})







def movie_detail(request):
    movies = Movie.objects.get(id=2)
    # context = 
    return HttpResponse(movies)

def genre_detail(request):
    genres = (Genre.objects.all())
    output = '    \n' .join([g.name for g in genres])
    return HttpResponse(output)
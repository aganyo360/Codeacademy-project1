from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Movie, Genre
# Create your views here.
def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies':movies})
def detail(request, movie_id):
   movie= get_object_or_404(Movie, pk=movie_id)
   return render(request,'movies/detail.html', {'movie': movie})





def movie_detail(request):
    movies = Movie.objects.get(id=2)
    # context = 
    return HttpResponse(movies)

def genre_detail(request):
    genres = (Genre.objects.all())
    output = '    \n' .join([g.name for g in genres])
    return HttpResponse(output)
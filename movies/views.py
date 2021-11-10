from django.shortcuts import render,redirect
from .models import Movie, Cast, Category
# from django.views.decorators.csrf import csrf_exempt
from .forms import MovieForm


# Create your views here.

def movie_index(request):
    all_movies = Movie.objects.all()
    print("ALL Movies ->", all_movies)
    return render(request, 'movie_index.html', context={'movies' : all_movies})


def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    return render(request, 'movie_detail.html', context={'movie': movie})

# def movie_create(request):
#     movie_name = request.POST.get('name')
#     movie_data = {'name':'Movie', 'description': 'Desc'}
#     movie_object = Movie.objects.create(**movie_data)
    # return render(request, 'movie_index.html', context={'movies' : all_movies})
def movie_create(request):
    form = MovieForm()
    print("REQUEST TYPE -> ", request.method)
    print(request.FILES)

    if request.method == 'POST':

        form = MovieForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            print("YES IS VALID")
            form.save()
            return redirect('movie:movie-index')

    return render(request, 'movie_create.html', context={'form': form})

def movie_delete(request, pk):
    Movie.objects.get(id=pk).delete()
    return redirect('movie:movie-index')

def movie_update(request, pk):
    movie = Movie.objects.get(id=pk)
    form = MovieForm(instance=movie)

    if request.method == 'POST':
        form = MovieForm(data=request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie:movie-detail', pk=movie.id)

    return render(request, 'movie_update.html', context={'form': form, 'movie': movie})


from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404

from .models import Movie
from .forms import MovieCreateForm
from django.views import View

# Create your views here.
def movie_create_view(request):
    form = MovieCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = MovieCreateForm()
    context = {
        "form": form
    }
    return render(request, "movies/movie_create.html", context)

def top_ten_view(request):
    queryset = Movie.objects.all()
    # ordered_queryset = queryset.order_by('review')
    context = {
        "object_list": queryset
    }
    return render(request, "movies/top_ten.html", context)

def movie_detail_view(request, id):
    try:
        obj = Movie.objects.get(id=id)
    except Article.DoesNotExist:
        raise Http404
    context = {
        "object": obj,
    }
    return render(request, "movies/movie_detail.html", context)

def movie_update_view(request, id):
    obj = get_object_or_404(Movie, id=id)
    form = MovieCreateForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        "form": form
    }
    return render(request, "movies/movie_create.html", context)

def movie_delete_view(request, id):
    obj = get_object_or_404(Movie, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, 'movies/movie_delete.html', context)


import json

from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, JsonResponse, HttpResponse

from .models import Movie, FilesAdmin
from .forms import MovieCreateForm, UserCreateForm
from .serializers import MovieSerializer, UserSerializer
from .decorators import unauthenticated_user, allowed_users
import random
import os


from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import mixins, generics
from django.contrib.auth.models import User, Group
from django.conf import settings
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required


# Create your views here.
## User views ##
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


##### CLASS BASED VIEWS ######

class MovieList(APIView):
    ''' List all movies, or create a new movie entry '''
    def get(self, request, format=None):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MovieDetail(APIView):
    ''' Retreive, update, or delete a movie instance '''
    def get_object(self, id):
        try:
            return Movie.objects.get(id=id)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        movie = self.get_object(id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        movie = self.get_object(id)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        snippet = self.get_object(id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, id):
        obj_to_patch = self.get_object(id)
        serializer = MovieSerializer(obj_to_patch, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)


###  VIEWS FOR WEBSITE FUNCTIONALITY #####
@login_required(login_url='login')
@allowed_users(allowed_roles=['admins'])
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
    except Movie.DoesNotExist:
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

def random_view(request):
    id = random.randint(0,10)
    try:
        obj = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        raise Http404
    context = {
        "id": obj.id,
        "title": obj.title,
        "year": obj.year,
        "description": obj.description,
        "rating": obj.rating,
        "ranking": obj.ranking,
        "review": obj.review,
        "img_url": obj.img_url
    }
    return JsonResponse(context)

def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type='application/adminupload')
            response['Content-Disposition'] = 'inline;filename=' + os.path.basename(file_path)
            return response
    raise Http404

@unauthenticated_user
def loginPage(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('top-ten')
        else:
            messages.info(request, 'Username Or Password is incorrect')

    context = {}
    return render(request, 'movies/login.html', context)

@unauthenticated_user
def register_user(request):
    form = UserCreateForm()
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='customers')
            user.groups.add(group)

            messages.success(request, 'Account was created for ' + username)
            return redirect("login")
    context = {'form': form}
    return render(request, 'movies/register.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admins'])
def secrets_view(request):
    context = {
        'file': FilesAdmin.objects.all()
    }
    return render(request, 'movies/secrets.html', context)


def logout_user(request):
    logout(request)
    return redirect("login")


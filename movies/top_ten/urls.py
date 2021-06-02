from django.contrib import admin
from django.urls import path, include

from .views import movie_create_view, movie_detail_view, top_ten_view, movie_update_view, movie_delete_view, random_view, MovieList, MovieDetail
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', top_ten_view, name="top-ten"),
    path('create/', movie_create_view, name="create-entry"),
    path('<int:id>/detail/', movie_detail_view, name="movie-detail"),
    path('<int:id>/update/', movie_update_view, name="movie-update"),
    path('<int:id>/delete/', movie_delete_view, name='movie-delete'),
    path('random/', random_view, name='random-movie'),
    path('all/', MovieList.as_view(), name='view-of-all'),
    path('detail/<int:id>/', MovieDetail.as_view(), name='details-of-movie'),
    # path('search/', search, name='search'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
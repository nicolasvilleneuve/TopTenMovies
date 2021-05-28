from django.contrib import admin
from django.urls import path, include

from .views import movie_create_view, movie_detail_view, top_ten_view, movie_update_view, movie_delete_view

urlpatterns = [
    path('', top_ten_view, name="top-ten"),
    path('create/', movie_create_view, name="create-entry"),
    path('<int:id>/detail/', movie_detail_view, name="movie-detail"),
    path('<int:id>/update/', movie_update_view, name="movie-update"),
    path('<int:id>/delete/', movie_delete_view, name='movie-delete'),
]
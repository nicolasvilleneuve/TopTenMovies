from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.static import serve

from .views import movie_create_view, movie_detail_view, top_ten_view, movie_update_view, movie_delete_view, random_view, \
    MovieList, MovieDetail, UserDetail, UserList, register_user, secrets_view, loginPage, logout_user
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', top_ten_view, name="top-ten"),
    path('create/', movie_create_view, name="create-entry"),
    path('<int:id>/detail/', movie_detail_view, name="movie-detail"),
    path('<int:id>/update/', movie_update_view, name="movie-update"),
    path('<int:id>/delete/', movie_delete_view, name='movie-delete'),
    path('random/', random_view, name='random-movie'),
    path('all/', MovieList.as_view(), name='view-of-all'),
    path('detail/<int:ranking>/', MovieDetail.as_view(), name='details-of-movie'),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>', UserDetail.as_view(), name='user-detail'),
    path('register/', register_user, name='register-user'),
    path('login/', loginPage, name='login'),
    path('logout/', logout_user, name='logout'),
    path('secrets/', secrets_view, name='secret-view'),
    url(r'^download/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
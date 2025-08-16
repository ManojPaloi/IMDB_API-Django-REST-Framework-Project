from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.api_root),
    path('list/', views.movie_list, name="movie-list"),
    path('list/<int:pk>/', views.movie_detail, name='movie-detail'),
    path('stream/', views.stream_list, name="stream-platform"),
    path('stream/<int:pk>/', views.stream_detail, name="streamplatform-detail"),
    path('reviews/', views.ReviewListView.as_view(), name='reviews_list'),
    path('reviews/<int:pk>/', views.ReviewDetailView.as_view(), name='reviews_detail'),

]

urlpatterns = format_suffix_patterns(urlpatterns)

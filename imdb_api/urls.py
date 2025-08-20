from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.api_root),
    path('list/', views.movie_list, name="movie-list"),
    path('list/<int:pk>/', views.movie_detail, name='movie-detail'),
    path('stream/', views.stream_list, name="stream-platform"),
    path('list/<int:pk>/review/', views.ReviewListView.as_view(), name="review-list"),
    path('list/<int:pk>/review-create/', views.ReviewCreateView.as_view(), name="review-create"),
    path('list/review/<int:pk>/', views.ReviewDetailView.as_view(), name='review-detail'),
] 

urlpatterns = format_suffix_patterns(urlpatterns)

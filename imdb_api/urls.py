from django.urls import path
from . import views

urlpatterns = [
    path ('list/', views.movie_list, name= "movie-list"),
    path ('list/<int:pk>', views.movie_detail, name='movie-detial'),
    path ('stream/', views.stream_list, name="strem-platform"),
    path ('stream/<int:pk>', views.stream_detail, name= "stream-platform-detail"),
    
    
    
]
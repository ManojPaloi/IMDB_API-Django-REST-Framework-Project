from django.http import JsonResponse
from .models import WatchList, StreamPlatform, Review
from .Serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework import generics
from rest_framework import serializers  
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly 



@api_view(['GET'])
@permission_classes([IsAdminUser])
def api_root(request, format=None):
    return Response({
        'movie-list': reverse('movie-list', request=request, format=format),
        'streamplatform-list': reverse('streamplatform-list', request=request, format=format)
    })






# Create your views here.
@permission_classes([IsAdminUser])
def movie_list(request):
    Movie_List = WatchList.objects.all()
    serializerd = WatchListSerializer(Movie_List, many = True, context={'request': request})

    return JsonResponse(serializerd.data, safe=False )

@permission_classes([IsAdminUser])
def movie_detail (request, pk):
    
    Movie_Details = WatchList.objects.get(pk=pk)
    serializerd = WatchListSerializer(Movie_Details, context={'request': request})

    return JsonResponse(serializerd.data)








@api_view(['GET', 'POST'])
@permission_classes([IsAdminUser])
def stream_list(request, format=None):
    print("stream_list view called with format =", format)
    if request.method == 'GET':
        Stream_List = StreamPlatform.objects.all()
        serializerd = StreamPlatformSerializer(Stream_List, many = True, context={'request': request})
        return Response(serializerd.data )
    
    elif request.method == 'POST':
        serializerd = StreamPlatformSerializer(data=request.data, context={'request': request})
        if serializerd.is_valid():
            serializerd.save()
            return Response(serializerd.data, status=status.HTTP_201_CREATED)
        return Response(serializerd.errors, status=status.HTTP_400_BAD_REQUEST) 

    
    
    

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly ])
def stream_detail(request, pk, format=None):
    print("stream_detail view called with format =", format)
    try:
        Stream_Detail = StreamPlatform.objects.get(pk=pk)
    except StreamPlatform.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StreamPlatformSerializer(Stream_Detail, context={'request': request})
        return Response(serializer.data)

    
    
    
    
    
    elif request.method == 'PUT':
        serializer = StreamPlatformSerializer(Stream_Detail, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Stream_Detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        
        
        
        
        
class ReviewListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated ]
    serializer_class = ReviewSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchList__pk=pk, active=True)


class ReviewCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        movie = WatchList.objects.get(pk=pk)
        user = self.request.user

        # Check if this user already reviewed this movie
        if Review.objects.filter(watchList=movie, review_user=user).exists():
            raise serializers.ValidationError("You have already reviewed this movie.")
        
        if movie.Average_rating == 0:
            movie.Average_rating = serializer.validated_data['rating']
        else:
            movie.Average_rating = (movie.Average_rating + serializer.validated_data['rating'])/2
        movie.Number_Rating +=1
        movie.save()
        serializer.save(watchList=movie, review_user=user)
        
        
        
        
        
    def create(self, request, *args, **kwargs):
        """Override to return full serialized data after creation"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)




class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly ]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

   
    




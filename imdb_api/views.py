from django.http import JsonResponse
from .models import WatchList, StreamPlatform
from .Serializers import WatchListSerializer, StreamPlatformSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
def movie_list(request):
    Movie_List = WatchList.objects.all()
    serializerd = WatchListSerializer(Movie_List, many = True)

    return JsonResponse(serializerd.data, safe=False )


def movie_detail (request, pk):
    
    Movie_Details = WatchList.objects.get(pk=pk)
    serializerd = WatchListSerializer(Movie_Details)

    return JsonResponse(serializerd.data)








@api_view(['GET', 'POST'])
def stream_list(request, format=None):
    print("stream_list view called with format =", format)
    if request.method == 'GET':
        Stream_List = StreamPlatform.objects.all()
        serializerd = StreamPlatformSerializer(Stream_List, many = True)
        return Response(serializerd.data )
    
    elif request.method == 'POST':
        serializerd = StreamPlatformSerializer(data=request.data)
        if serializerd.is_valid():
            serializerd.save()
            return Response(serializerd.data, status=status.HTTP_201_CREATED)
        return Response(serializerd.errors, status=status.HTTP_400_BAD_REQUEST) 

    
    
    

@api_view(['GET', 'PUT', 'DELETE'])
def stream_detail(request, pk, format=None):
    print("stream_detail view called with format =", format)
    try:
        Stream_Detail = StreamPlatform.objects.get(pk=pk)
    except StreamPlatform.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StreamPlatformSerializer(Stream_Detail)
        return Response(serializer.data)

    
    
    
    
    
    elif request.method == 'PUT':
        serializer = StreamPlatformSerializer(Stream_Detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Stream_Detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        




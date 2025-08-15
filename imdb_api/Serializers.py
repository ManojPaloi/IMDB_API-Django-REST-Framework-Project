from rest_framework import serializers
from .models import WatchList, StreamPlatform


class WatchListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField ( view_name = 'movie-detail')
    class Meta:
        model = WatchList
        fields = '__all__'

class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField ( view_name = 'streamplatform-detail')
    watchList = WatchListSerializer(many =True, read_only= True)
    class Meta:
        model = StreamPlatform
        fields = '__all__'

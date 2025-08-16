from rest_framework import serializers
from .models import WatchList, StreamPlatform, Review


class WatchListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField ( view_name = 'movie-detail')
    class Meta:
        model = WatchList
        fields = '__all__'
        
        
        
    def validate_name (self, value):
        
        if  len(value)<=2:
            raise serializers.ValidationError("Blog post is not about Django")
        return value
        
        
        
    def validate(self, data):
         
        if data['name'] == data['about']:
            raise serializers.ValidationError("filed both is same name and about")
        return data
        

class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField ( view_name = 'streamplatform-detail')
    watchList = WatchListSerializer(many =True, read_only= True)
    class Meta:
        model = StreamPlatform
        fields = '__all__'
 
 
 
 
 
class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        
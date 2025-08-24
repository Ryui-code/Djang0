from rest_framework import serializers
from .models import *


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model=Country
        fields = '__all__'


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Actor
        fields = '__all__'


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Director
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rating
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    actor = ActorSerializer(read_only=True)
    director = DirectorSerializer(read_only=True)
    rating = RatingSerializer(read_only=True)
    country = CountrySerializer(read_only=True)
    class Meta:
        model=Movie
        fields = '__all__'
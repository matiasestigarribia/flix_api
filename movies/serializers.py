from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie
from genres.serializers import GenreSerializer
from actors.serializers import ActorSerializer

class MovieModelSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Movie
        fields = ('__all__')


    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError('Release date can not be before 1900')
        return value

    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError('Resume can not be longer than 500 characters')
        return value

class MovieListDetailSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)
    
    def get_rate(self, obj):
        actors = ActorSerializer(many=True)
        genre = GenreSerializer()
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)

        return None
    
    class Meta:
        model = Movie
        fields = ['id', 'tittle', 'genre', 'actors', 'release_date', 'rate', 'resume']


class MovieStatsSerializer(serializers.Serializer):
    total_movies = serializers.IntegerField()
    movies_by_genre = serializers.ListField()
    total_reviews = serializers.IntegerField()
    average_stars = serializers.FloatField()

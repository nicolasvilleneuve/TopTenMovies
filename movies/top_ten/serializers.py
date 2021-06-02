from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id',
                  'title',
                  'year',
                  'description',
                  'rating',
                  'ranking',
                  'review',
                  'img_url']

    def create(self, validated_data):
        """Create and return a new 'Movie' instance, given the validated data"""
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Update and return an existing 'Movie' instance, given the validated data"""
        instance.title = validated_data.get('title', instance.title)
        instance.year = validated_data.get('year', instance.year)
        instance.description = validated_data.get('description', instance.description)
        instance.ranking = validated_data.get('ranking', instance.ranking)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.review = validated_data.get('review', instance.review)
        instance.img_url = validated_data.get('img_url', instance.img_url)
        instance.save()
        return instance

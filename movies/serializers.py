from rest_framework import serializers
from .models import Movie
from drf_extra_fields.fields import Base64ImageField

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    poster = Base64ImageField()
    class Meta:
        model = Movie
        fields = '__all__'

class MovieFirstStepSerializer(serializers.Serializer):
    title = serializers.CharField()
    release_date = serializers.DateField()
    studio = serializers.CharField()
    class Meta:
        fields = '__all__'

class MovieSecondStepSerializer(serializers.HyperlinkedModelSerializer):
    pk = serializers.IntegerField()
    poster = Base64ImageField(required = False)
    duration = serializers.DurationField()
    class Meta:
        model = Movie
        fields = ('pk','poster', 'desc', 'duration')

class MovieThirdStepSerializer(serializers.HyperlinkedModelSerializer):
    pk = serializers.IntegerField()
    class Meta:
        model = Movie
        fields = ('pk','film_file',)


# {
# "title": "Test8",
# "release_date": "2001-04-13',
# "studio": "ABS"
# }
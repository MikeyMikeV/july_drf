from django.shortcuts import render
from rest_framework import permissions, viewsets
from .models import Movie
from . import serializers
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from datetime import timedelta, datetime
from braces.views import CsrfExemptMixin
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def home_page(request):
    return render(request, 'base.html', {})

@csrf_exempt
def first_step(request):
    return render(request, 'movie_creation/first_step.html', {})

@csrf_exempt
def second_step(request, film_id):
    return render(request, 'movie_creation/second_step.html', {})

@csrf_exempt
def third_step(request,film_id):
    return render(request, 'movie_creation/third_step.html', {})

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = serializers.MovieSerializer
    permission_classes = [permissions.AllowAny]

from rest_framework.response import Response

class MovieFirstStepViewSet(CsrfExemptMixin, viewsets.ViewSet):
    serializer_class = serializers.MovieFirstStepSerializer
    permission_classes = [permissions.AllowAny]
    parser_classes = (JSONParser,MultiPartParser)
    authentication_classes = []

    def list(self, request):
        return Response('First Step')
    
    def create(self, request):
        title = request.data['title']
        release_date = request.data['release_date']
        studio = request.data['studio']
        film = Movie.objects.create(title=title, release_date=release_date, studio=studio)
        film.save()
        return Response({
            'film_id':film.pk
        })
    

class MovieSecondStepViewSet(viewsets.ViewSet):
    serializer_class = serializers.MovieSecondStepSerializer
    permission_classes = [permissions.AllowAny]
    parser_classes = (JSONParser,FormParser, MultiPartParser)
    # queryset = Movie.objects.filter(poster = None)
    
    def list(self, request):
        return Response(serializers.MovieSecondStepSerializer(Movie.objects.filter(poster=''),many=True).data)
    
    def create(self, request):
        film_id = request.data['pk']
        poster = request.data['poster']
        desc = request.data['desc']
        duration = request.data['duration']
        print(Movie.objects.get(pk=1).duration, type(Movie.objects.get(pk=1).duration))
        film = Movie.objects.get(pk = film_id)
        film.poster = poster
        film.desc = desc
        t = datetime.strptime(duration,'%H:%M:%S')
        film.duration = timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
        film.save()
        return Response("File uploaded")

# ДАУРИЯ ДОДЕЛАТЬ
class MovieThirdStepViewSet(viewsets.ViewSet):
    serializer_class = serializers.MovieThirdStepSerializer
    permission_classes = [permissions.AllowAny]
    parser_classes = (JSONParser,FormParser, MultiPartParser)
    # queryset = Movie.objects.filter(poster = None)
    
    def list(self, request):
        return Response(serializers.MovieThirdStepSerializer(Movie.objects.filter(film_file=''),many=True).data)

    def create(self, request):
        film_id = request.data['pk']
        file_upload = request.data['film_file']
        film = Movie.objects.get(pk = film_id)
        film.film_file = file_upload
        film.save()
        return Response("File uploaded")
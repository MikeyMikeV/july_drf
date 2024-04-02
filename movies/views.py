from django.shortcuts import render
from rest_framework import permissions, viewsets
from .models import Movie
from . import serializers
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser


def home_page(request):
    return render(request, 'base.html', {})

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = serializers.MovieSerializer
    permission_classes = [permissions.AllowAny]
    # parser_classes = [JSONParser, MultiPartParser]

from rest_framework.response import Response

class MovieFirstStepViewSet(viewsets.ViewSet):
    serializer_class = serializers.MovieFirstStepSerializer
    permission_classes = [permissions.AllowAny]
    parser_classes = (JSONParser,FormParser, MultiPartParser)

    def list(self, request):
        return Response('First Step')
    
    def create(self, request):
        title = request.data['title']
        release_date = request.data['release_date']
        studio = request.data['studio']
        film = Movie.objects.create(title=title, release_date=release_date, studio=studio)
        film.save()
        return Response("File uploaded")
        

class MovieSecondStepViewSet(viewsets.ViewSet):
    serializer_class = serializers.MovieSecondStepSerializer
    permission_classes = [permissions.AllowAny]
    parser_classes = (JSONParser,FormParser, MultiPartParser)
    # queryset = Movie.objects.filter(poster = None)
    
    def list(self, request):
        return Response(serializers.MovieSecondStepSerializer(Movie.objects.filter(poster=''),many=True).data)
    
    def create(self, request):
        film_id = request.data['pk']
        film = Movie.objects.get(pk = film_id)
        ser = serializers.MovieSecondStepSerializer(instance=film,data=request.data)
        if ser.is_valid():
            ser.save()
            return Response("File uploaded", 201)
        return Response("Error", 400)

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
        film = Movie.objects.get(pk = film_id)
        ser = serializers.MovieSecondStepSerializer(instance=film,data=request.data)
        if ser.is_valid():
            ser.save()
            return Response("File uploaded", 201)
        return Response("Error", 400)
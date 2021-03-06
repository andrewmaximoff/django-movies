# -*- coding: utf-8 -*-

from django.shortcuts import render
from rest_framework import viewsets
from movies.models import Movie
from movies.serializers import MovieSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
def index(request):
    return render(request, 'index.html', {})
    
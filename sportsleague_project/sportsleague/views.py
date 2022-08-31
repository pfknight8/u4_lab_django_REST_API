from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import  generics
from .serializers import ConferenceSerializer, DivisionSerializer, TeamSerializer, PlayerSerializer
from .models import Conference, Division, Team, Player

# Create your views here.
class ConferenceList(generics.ListCreateAPIView):
  queryset = Conference.objects.all()
  serializer_class = ConferenceSerializer

class DivisionList(generics.ListCreateAPIView):
  queryset = Division.objects.all()
  serializer_class = DivisionSerializer

class TeamList(generics.ListCreateAPIView):
  queryset = Team.objects.all()
  serializer_class = TeamSerializer

class PlayerList(generics.ListCreateAPIView):
  queryset = Player.objects.all()
  serializer_class = PlayerSerializer

class ConferenceDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Conference.objects.all()
  serializer_class = ConferenceSerializer

class DivisionDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Division.objects.all()
  serializer_class = DivisionSerializer

class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Team.objects.all()
  serializer_class = TeamSerializer

class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Player.objects.all()
  serializer_class = PlayerSerializer  
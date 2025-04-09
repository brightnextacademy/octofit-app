from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': 'https://[fantastic-space-barnacle-r4pg5xpwpxwxcw5j6]-8000.app.github.dev/api/users/',
        'teams': 'https://[fantastic-space-barnacle-r4pg5xpwpxwxcw5j6]-8000.app.github.dev/api/teams/',
        'activities': 'https://[fantastic-space-barnacle-r4pg5xpwpxwxcw5j6]-8000.app.github.dev/api/activities/',
        'leaderboard': 'https://[fantastic-space-barnacle-r4pg5xpwpxwxcw5j6]-8000.app.github.dev/api/leaderboard/',
        'workouts': 'https://[fantastic-space-barnacle-r4pg5xpwpxwxcw5j6]-8000.app.github.dev/api/workouts/'
    })

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

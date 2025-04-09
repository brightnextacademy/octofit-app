import json
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        with open('octofit_tracker/test_data.json', 'r') as file:
            data = json.load(file)

        # Create users
        for user_data in data['users']:
            User.objects.create_user(
                username=user_data['username'],
                email=user_data['email'],
                password=user_data['password']
            )

        # Create teams
        for team_data in data['teams']:
            team = Team.objects.create(name=team_data['name'])
            for member_username in team_data['members']:
                user = User.objects.get(username=member_username)
                team.members.add(user)

        # Create activities
        for activity_data in data['activities']:
            user = User.objects.get(username=activity_data['user'])
            Activity.objects.create(
                user=user,
                activity=activity_data['activity'],
                duration=activity_data['duration']
            )

        # Create leaderboard entries
        for leaderboard_data in data['leaderboard']:
            team = Team.objects.get(name=leaderboard_data['team'])
            Leaderboard.objects.create(
                team=team,
                points=leaderboard_data['points']
            )

        # Create workouts
        for workout_data in data['workouts']:
            Workout.objects.create(
                name=workout_data['name'],
                description=workout_data['description']
            )

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))

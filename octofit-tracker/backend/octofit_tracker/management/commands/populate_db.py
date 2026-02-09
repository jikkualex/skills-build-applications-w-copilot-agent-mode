from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel')
        dc = Team.objects.create(name='dc')

        # Create users
        users = [
            User(name='Tony Stark', email='tony@marvel.com', team='marvel'),
            User(name='Steve Rogers', email='steve@marvel.com', team='marvel'),
            User(name='Bruce Wayne', email='bruce@dc.com', team='dc'),
            User(name='Clark Kent', email='clark@dc.com', team='dc'),
        ]
        for user in users:
            user.save()

        # Create activities
        activities = [
            Activity(user='Tony Stark', activity_type='Running', duration=30, date='2026-02-09'),
            Activity(user='Steve Rogers', activity_type='Cycling', duration=45, date='2026-02-08'),
            Activity(user='Bruce Wayne', activity_type='Swimming', duration=25, date='2026-02-07'),
            Activity(user='Clark Kent', activity_type='Flying', duration=60, date='2026-02-06'),
        ]
        for activity in activities:
            activity.save()

        # Create leaderboard
        Leaderboard.objects.create(team='marvel', points=150)
        Leaderboard.objects.create(team='dc', points=120)

        # Create workouts
        workouts = [
            Workout(name='Pushups', description='Upper body strength', difficulty='Easy'),
            Workout(name='Squats', description='Lower body strength', difficulty='Medium'),
            Workout(name='Plank', description='Core strength', difficulty='Hard'),
        ]
        for workout in workouts:
            workout.save()

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))

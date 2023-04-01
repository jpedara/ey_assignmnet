import random
import pytz
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from users.models import User, ActivityPeriod


class Command(BaseCommand):
    help = 'Populates the database with dummy data'

    def add_arguments(self, parser):
        parser.add_argument('users', type=int, help='The number of users to create')
        parser.add_argument('activities', type=int, help='The number of activities to create for each user')

    def handle(self, *args, **options):
        users_count = options['users']
        activities_count = options['activities']

        for i in range(users_count):
            user = User.objects.create(
                id=f'W0{i+1}2ABC{i+1}',
                real_name=f'User {i+1}',
                tz=random.choice(pytz.all_timezones)
            )

            for j in range(activities_count):
                start_time = timezone.now() - timezone.timedelta(days=random.randint(1, 365))
                end_time = start_time + timezone.timedelta(minutes=random.randint(30, 120))

                ActivityPeriod.objects.create(
                    user=user,
                    start_time=start_time,
                    end_time=end_time
                )

        self.stdout.write(self.style.SUCCESS(f'Successfully created {users_count} users and {users_count * activities_count} activities'))

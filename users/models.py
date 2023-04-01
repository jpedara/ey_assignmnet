from django.db import models

class User(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    real_name = models.CharField(max_length=255)
    tz = models.CharField(max_length=255)

    def __str__(self):
        return self.real_name

class ActivityPeriod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activity_periods')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.user.real_name}'s activity period from {self.start_time} to {self.end_time}"

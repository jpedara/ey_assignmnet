from rest_framework import serializers
from users.models import User, ActivityPeriod


class ActivityPeriodSerializer(serializers.ModelSerializer):
    start_time = serializers.SerializerMethodField()
    end_time = serializers.SerializerMethodField()

    def get_start_time(self, obj):
        return obj.start_time.strftime("%b %d %Y %I:%M %p")

    def get_end_time(self, obj):
        return obj.end_time.strftime("%b %d %Y %I:%M %p")
    
    class Meta:
        model = ActivityPeriod
        fields = ('start_time', 'end_time')


class UserSerializer(serializers.ModelSerializer):
    activity_periods = ActivityPeriodSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'real_name', 'tz', 'activity_periods')

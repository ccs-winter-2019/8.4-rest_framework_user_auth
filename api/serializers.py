from rest_framework.serializers import ModelSerializer

from rides.models import Ride


class RideSerializer(ModelSerializer):
    class Meta:
        model = Ride
        fields = ('participant_count', 'ride_date', 'duration', 'horse')
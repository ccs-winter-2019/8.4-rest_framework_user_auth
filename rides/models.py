from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Ride(models.Model):
    HALF_HOUR_DURATION = '30'
    ONE_HOUR_DURATION = '60'
    TWO_HOUR_DURATION = '120'

    DURATION_CHOICES = (
        (HALF_HOUR_DURATION, '30 Min'),
        (ONE_HOUR_DURATION, '1 Hour'),
        (TWO_HOUR_DURATION, '2 Hours'),
    )

    participant_count = models.IntegerField(default=1)
    duration = models.CharField(choices=DURATION_CHOICES, max_length=3)
    ride_date = models.DateTimeField()
    horse = models.ForeignKey('rides.Horse', null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.PROTECT)


class Horse(models.Model):
    name = models.CharField(max_length=255)
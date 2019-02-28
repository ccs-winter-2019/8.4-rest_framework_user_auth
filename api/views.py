from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication

from .serializers import RideSerializer
from rides.models import Ride, Horse


class CsrfExemptMixin(SessionAuthentication):
    def enforce_csrf(self, request):
        return # do nothing... thanks


class RideViewSet(ModelViewSet):
    serializer_class = RideSerializer
    queryset = Ride.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (CsrfExemptMixin, )

    def perform_create(self, serializer):
        horse = Horse.objects.order_by('?').first()
        serializer.save(horse=horse, user=self.request.user)

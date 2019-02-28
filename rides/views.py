import os

from django.views.generic import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.conf import settings

from .models import Ride


class RideListView(LoginRequiredMixin, ListView):

    def get_queryset(self):
        return Ride.objects.filter(user=self.request.user)


class RideCreateView(LoginRequiredMixin, View):
    """
    Serves the compiled frontend entry point (only works if you have run `yarn
    run build`).
    """

    def get(self, request):
        try:
            with open(os.path.join('frontend/static', 'build', 'index.html')) as f:
                return HttpResponse(f.read())
        except FileNotFoundError:
            return HttpResponse(
                """
                This URL is only used when you have built the production
                version of the app. Visit http://localhost:3000/ instead, or
                run `yarn run build` to test the production version.
                """,
                status=501,
            )

from django.urls import path, include

from .views import RideListView, RideCreateView

app_name = 'rides'

urlpatterns = [
    path('rides/', RideListView.as_view(), name='ride_list'),
    path('rides/book/', RideCreateView.as_view(), name='ride_create'),
]
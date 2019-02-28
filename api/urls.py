from django.urls import path, include
from rest_framework import routers

from .views import RideViewSet

router = routers.SimpleRouter()
router.register(r'rides', RideViewSet)

urlpatterns = router.urls
urlpatterns += [
    path('auth/', include('rest_framework.urls')),
]
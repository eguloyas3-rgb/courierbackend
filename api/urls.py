from django.urls import path
from .views import *

urlpatterns = [
    path("tracking/<str:tracking_id>/", TrackingAPIView.as_view(), name="tracking-api"),
    # path("tracking/all/", TrackingAllAPIView.as_view(), name="tracking-all-api"),
    path("contact/", ContactAPIView.as_view(), name="contact-api"),
    path("ping/", PingAPIView.as_view(), name="ping"),
]



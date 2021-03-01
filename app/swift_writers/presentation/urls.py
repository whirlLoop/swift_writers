from django.urls import path
from swift_writers.presentation.landing_page import LandingPageView

app_name = 'swift_writers'

urlpatterns = [
    path('', LandingPageView.as_view(), name='index'),
]

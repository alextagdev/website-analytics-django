# notes/urls.py

from django.urls import path
from .views import analyze_performance, analysis_results
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', analyze_performance, name='analyze_performance'),
    path('web/', RedirectView.as_view(pattern_name='analyze_performance', permanent=True)),
    path('analysis_results/', analysis_results, name='analysis_results'),
    # Alte căi ale aplicației tale...
]

from django.urls import path
from .views import ContinentView, CountryView, RegionView, PlaceView, RaceView, SubRaceView, TribeView, PlaceListView

urlpatterns = [
    path('continent/', ContinentView.as_view()),
    path('country/', CountryView.as_view()),
    path('region/', RegionView.as_view()),
    path('place/', PlaceView.as_view()),
    path('places/', PlaceListView.as_view()),
    path('race/', RaceView.as_view()),
    path('subrace/', SubRaceView.as_view()),
    path('tribe/', TribeView.as_view())
]

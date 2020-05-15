from django.conf import settings
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_201_CREATED, HTTP_422_UNPROCESSABLE_ENTITY, HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED

from .models import Continent, Country, Region, Place, Race, SubRace, Tribe
from .serializers import ContinentSerializer, CountrySerializer, RegionSerializer, PlaceSerializer, RaceSerializer, SubRaceSerializer, TribeSerializer, PopulatedPlaceSerializer, PopulatedRegionSerializer, PopulatedCountrySerializer

class ContinentView(APIView):

    def get(self, _request):
        continent = Continent.objects.all()
        serializer = ContinentSerializer(continent, many=True)
        return Response(serializer.data)

    def post(self, request):
        continent = ContinentSerializer(data=request.data)
        if continent.is_valid():
            continent.save()
            return Response(continent.data, status=HTTP_201_CREATED)
        return Response(continent.errors, status=HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, _request, pk):
        continent = Continent.objects.get(pk=pk)
        continent.delete()
        return Response(status=HTTP_204_NO_CONTENT)

class CountryView(APIView):

    def get(self, _request):
        country = Country.objects.all()
        serializer = CountrySerializer(country, many=True)
        return Response(serializer.data)

    def post(self, request):
        country = CountrySerializer(data=request.data)
        if country.is_valid():
            country.save()
            return Response(country.data, status=HTTP_201_CREATED)
        return Response(country.errors, status=HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, _request, pk):
        country = Country.objects.get(pk=pk)
        country.delete()
        return Response(status=HTTP_204_NO_CONTENT)

class RegionView(APIView):

    def get(self, _request):
        region = Region.objects.all()
        serializer = RegionSerializer(region, many=True)
        return Response(serializer.data)

    def post(self, request):
        region = RegionSerializer(data=request.data)
        if region.is_valid():
            region.save()
            return Response(region.data, status=HTTP_201_CREATED)
        return Response(region.errors, status=HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, _request, pk):
        region = Region.objects.get(pk=pk)
        region.delete()
        return Response(status=HTTP_204_NO_CONTENT)

class PlaceView(APIView):

    def get(self, _request):
        place = Place.objects.all()
        serializer = PlaceSerializer(place, many=True)
        return Response(serializer.data)

    def post(self, request):
        place = PlaceSerializer(data=request.data)
        if place.is_valid():
            place.save()
            return Response(place.data, status=HTTP_201_CREATED)
        return Response(place.errors, status=HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, _request, pk):
        place = Place.objects.get(pk=pk)
        place.delete()
        return Response(status=HTTP_204_NO_CONTENT)

class RaceView(APIView):

    def get(self, _request):
        race = Race.objects.all()
        serializer = RaceSerializer(race, many=True)
        return Response(serializer.data)

    def post(self, request):
        race = RaceSerializer(data=request.data)
        if race.is_valid():
            race.save()
            return Response(race.data, status=HTTP_201_CREATED)
        return Response(race.errors, status=HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, _request, pk):
        race = Race.objects.get(pk=pk)
        race.delete()
        return Response(status=HTTP_204_NO_CONTENT)

class SubRaceView(APIView):

    def get(self, _request):
        subrace = SubRace.objects.all()
        serializer = SubRaceSerializer(subrace, many=True)
        return Response(serializer.data)

    def post(self, request):
        subrace = SubRaceSerializer(data=request.data)
        if subrace.is_valid():
            subrace.save()
            return Response(subrace.data, status=HTTP_201_CREATED)
        return Response(subrace.errors, status=HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, _request, pk):
        subrace = SubRace.objects.get(pk=pk)
        subrace.delete()
        return Response(status=HTTP_204_NO_CONTENT)

class TribeView(APIView):

    def get(self, _request):
        tribe = Tribe.objects.all()
        serializer = TribeSerializer(tribe, many=True)
        return Response(serializer.data)

    def post(self, request):
        tribe = TribeSerializer(data=request.data)
        if tribe.is_valid():
            tribe.save()
            return Response(tribe.data, status=HTTP_201_CREATED)
        return Response(tribe.errors, status=HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, _request, pk):
        tribe = Tribe.objects.get(pk=pk)
        tribe.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class PlaceListView(APIView):

    def get(self, _request):
        place = Place.objects.all()
        place_serializer = PopulatedPlaceSerializer(place, many=True)

        return Response({
            'place': place_serializer.data,
        })

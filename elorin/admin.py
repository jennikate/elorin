from django.contrib import admin
from .models import Continent, Country, Region, Place, Race, SubRace, Tribe

# Register your models here.
admin.site.register(Continent)
admin.site.register(Country)
admin.site.register(Region)
admin.site.register(Place)
admin.site.register(Race)
admin.site.register(SubRace)
admin.site.register(Tribe)

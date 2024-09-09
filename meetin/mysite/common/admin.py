from django.contrib import admin
from .models import Info, menInfo, womenInfo, matchingInfo, Location

admin.site.register(Info)
admin.site.register(menInfo)
admin.site.register(womenInfo)
admin.site.register(matchingInfo)
admin.site.register(Location)
from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Place)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(District)
admin.site.register(CustomUser)
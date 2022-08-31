from django.contrib import admin
from .models import Conference, Division, Team, Player

# Register your models here.
admin.site.register(Conference)
admin.site.register(Division)
admin.site.register(Team)
admin.site.register(Player)
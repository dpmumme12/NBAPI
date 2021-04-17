from django.contrib import admin
from .models import User, players, statistics

# Register your models here.

admin.site.register(User)
admin.site.register(players)
admin.site.register(statistics)
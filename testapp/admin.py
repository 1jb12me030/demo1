from django.contrib import admin
from testapp.models import *

# Register your models here.
admin.site.register(GameCategory)

admin.site.register(Game)
admin.site.register(Player)
admin.site.register(PlayerScore)


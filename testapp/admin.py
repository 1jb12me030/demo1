from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(employes)
admin.site.register(company)
admin.site.register(projects)
from django.contrib import admin
from .models import Listing  # whatever you had in models of this app

# Register your models here.
admin.site.register(Listing)
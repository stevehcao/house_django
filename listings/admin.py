from django.contrib import admin
from .models import Listing  # whatever you had in models of this app


# creating class here will allow you to change the display of the admin table
# in the admin section of the django app
# have to pass it in the register
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date',
                    'realtor')
    list_display_links = ('id', 'title')
    # one comma because of tuple restrictions
    list_filter = ('realtor', )
    list_editable = ('is_published', )
    search_fields = ('title', 'description', 'address', 'city', 'state',
                     'zipcode', 'price')
    list_per_page = 25


# Register your models here.
admin.site.register(Listing, ListingAdmin)
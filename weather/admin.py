# -*- coding: utf-8 -*-

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

from .models import Country, City

class HemisphereFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
#    title = 'Полушарие Земли'
    title = _('The hemisphere of the Earth')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'hemisphere'


    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('East', _('East hemisphere')),
            ('West', _('West hemisphere')),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == 'East':
            return queryset.filter(coord_lon__gte=0)
        if self.value() == 'West':
            return queryset.filter(coord_lon__lte=0)


class CountryAdmin(admin.ModelAdmin):
    list_display = ('brief', 'name')
    list_editable = ['name']
    search_fields = ['brief', 'name']
 
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country','coord_lon','coord_lat')
    fieldsets = [
        (None,               {'fields': ['name','country']}),
        ('Координаты', {'fields': [('coord_lon','coord_lat')]}),
    ]
    search_fields = ['name']
    list_filter = (HemisphereFilter,'country',)
    
    
    def view_country(self, obj):
        return obj.country
        
    view_country.short_name = 'страна' 
    view_country.empty_value_display = '-- не указана --'

# Register the admin class with the associated model
admin.site.register(City,CityAdmin)
admin.site.register(Country, CountryAdmin)
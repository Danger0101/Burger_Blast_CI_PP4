'''
This file is used to register the Meal model with the Django admin
so that we can manage the meals from the admin interface.
'''
from django.contrib import admin
from .models import Meal


class MealAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'calories',
        'preparation_time'
    )
    list_filter = ('category',)
    search_fields = ('name', 'description')
    readonly_fields = ('slug',)
    fieldsets = (
        (None, {
            'fields': (
                'name',
                'description',
                'category',
                'people',
                'price',
                'calories',
                'allergens',
                'preparation_time'
            )
        }),
        ('Slug', {
            'fields': ('slug',),
            'classes': ('collapse',)
        }),
    )


admin.site.register(Meal, MealAdmin)

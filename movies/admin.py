# -*- coding: utf-8 -*-

from django.contrib import admin
from movies.models import *

class AwardAdmin(admin.ModelAdmin):
    list_display = ['name', 'presented_by', 'country', 'formation']
    ordering = ['name']
    prepopulated_fields = {'slug': ('name',)}
    
class AwardCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'first_awarded', 'awarded_for']
    ordering = ['name']
    prepopulated_fields = {'slug': ('name',)}
    
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    list_filter = (('country', admin.RelatedOnlyFieldListFilter),)
    ordering = ['name']
    prepopulated_fields = {'slug': ('name',)}
    
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'code']
    ordering = ['name']
    prepopulated_fields = {'slug': ('name',)}
    
class FestivalAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'city', 'founded', 'description']
    ordering = ['name']
    prepopulated_fields = {'slug': ('name',)}
    
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    ordering = ['name']
    prepopulated_fields = {'slug': ('name',)}

class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'code']
    ordering = ['name']
    prepopulated_fields = {'slug': ('name',)}

class MovieAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'name_es',
        'director', 'release_date',
        'language', 'image'
    ]
    list_filter = (
        ('director', admin.RelatedOnlyFieldListFilter),
        ('language', admin.RelatedOnlyFieldListFilter),
        ('release_date'),
    )
    ordering = ['name']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']
    
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'abbreviation', 'country', 'formation']
    ordering = ['name']
    prepopulated_fields = {'slug': ('name',)}

class PersonAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'slug', 'birth_date', 'country', 'image']
    list_filter = (
        ('person_type', admin.RelatedOnlyFieldListFilter),
        ('country', admin.RelatedOnlyFieldListFilter),
    )
    prepopulated_fields = {'slug': ('first_name', 'last_name')}
    search_fields = ['first_name', 'last_name']

class PersonTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    ordering = ['name']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Award, AwardAdmin)
admin.site.register(AwardCategory, AwardCategoryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Festival, FestivalAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(PersonType, PersonTypeAdmin)
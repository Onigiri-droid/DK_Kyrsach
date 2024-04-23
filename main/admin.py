from django.contrib import admin
from .models import *


@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('title', 'programs_start', 'programs_end', 'description', 'slug')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('competition', 'rating', 'created_at')
    list_filter = ('competition', 'rating')
    search_fields = ('competition__title', 'comment')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'start', 'description', 'competition')
    list_filter = ('competition',)
    search_fields = ('title', 'description')


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('address', 'phone', 'mail')
    search_fields = ('address', 'phone', 'mail')

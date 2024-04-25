from django.contrib import admin
from .models import *


@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('title', 'programs_start', 'programs_end', 'description', 'contacts', 'age')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('rating', 'comment', 'created_at')
    filter_horizontal = ('lesson',)
    search_fields = ('comment',)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'contacts')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('address', 'phone', 'mail')
    search_fields = ('address', 'phone', 'mail')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'age', 'having_place', 'duration_lesson', 'cost_lesson', 'repetitions_week', 'duration_training')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Age)
class AgeAdmin(admin.ModelAdmin):
    list_display = ('participants',)
    search_fields = ('participants',)


@admin.register(Having)
class HavingAdmin(admin.ModelAdmin):
    list_display = ('place',)
    search_fields = ('place',)


@admin.register(Time)
class TimeAdmin(admin.ModelAdmin):
    list_display = ('duration',)
    search_fields = ('duration',)
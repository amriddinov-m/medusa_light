from django.contrib import admin

from news.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = 'subject', 'date', 'content'
    list_filter = 'date',

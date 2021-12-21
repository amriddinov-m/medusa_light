from django.contrib import admin

from news.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = 'title', 'published_date', 'content'
    list_filter = 'published_date',

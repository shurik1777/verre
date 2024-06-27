from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'photo')
    list_display_links = ('name',)
    search_fields = ('name', 'description')
    # readonly_fields = ('photo',)  # - Чтобы сделать поле "photo" редактируемым в админке, удалите его из readonly_fields.

    def photo(self, obj):
        if obj.photo:
            return mark_safe('<img src="{}" width="100" height="100" />'.format(obj.photo.url))
        else:
            return 'No Photo'

    photo.allow_tags = True

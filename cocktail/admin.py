from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category

admin.site.site_header = 'Verre - сайт рецептов алкогольных напитков'
admin.site.site_title = 'Администрирование сайта'
admin.site.index_title = 'Администрирование сайта'



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_display_links = ('name',)
    search_fields = ('name', 'description')
    # readonly_fields = ('photo',)  # - Чтобы сделать поле "photo" не редактируемым в админке, раскомментировать строку.
    #
    # def photo(self, obj):
    #     if obj.photo:
    #         return mark_safe('<img src="{}" width="100" height="100" />'.format(obj.photo.url))
    #     else:
    #         return 'No Photo'
    #
    # photo.allow_tags = True

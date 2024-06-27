from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Ingredient

admin.site.site_header = 'Verre - сайт рецептов алкогольных напитков'
admin.site.site_title = 'Администрирование сайта'
admin.site.index_title = 'Администрирование сайта'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'description')
    list_display_links = ('name',)
    search_fields = ('name', 'description')


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "description", "image"]
    list_editable = ["description", ]
    search_fields = ["name", "description"]
    list_filter = ["name", "description"]
    # readonly_fields = ('image',)  # - Чтобы сделать поле "image" не редактируемым в админке, раскомментировать строку.

    def image(self, obj):
        if obj.image:
            return mark_safe('<img src="{}" width="100" height="100" />'.format(obj.photo.url))
        else:
            return 'No image'

    image.allow_tags = True
    fields = [
        "name",
        "slug",
        "description",
        "image",
        "category",
    ]

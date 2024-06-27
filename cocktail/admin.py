from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Ingredient, Unit, Recipe, RecipeIngredient

admin.site.site_header = 'Verre - сайт рецептов алкогольных напитков'
admin.site.site_title = 'Администрирование сайта'
admin.site.index_title = 'Администрирование сайта'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'description', "slug")
    list_display_links = ('name',)
    list_editable = ["slug", ]
    search_fields = ('name', 'description', "slug")
    fields = [
        "name",
        "slug",
        "description",
    ]


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


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('u_name', 'u_anno')
    list_editable = ['u_anno', ]
    # list_display_links = ('u_name',)
    search_fields = ('u_anno',)
    fields = [
        "u_name",
        "u_anno",
    ]


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['title', 'author', 'preparation_time', 'image']
    list_display_links = ('title',)
    search_fields = ('title', 'description', 'author')
    readonly_fields = ('image',)
    fields = [
        "title",
        "slug",
        "description",
        "preparation_steps",
        "preparation_time",
        "image",
        "author",
    ]

    def image(self, obj):
        if obj.image:
            return mark_safe('<img src="{}" width="100" height="100" />'.format(obj.image.url))
        else:
            return 'No image'

    image.allow_tags = True


@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient', 'unit', 'register_date')
    list_filter = ('recipe',)
    search_fields = ('ingredient__name',)
    fields = [
        "recipe",
        "ingredient",
        "unit",
    ]

    # Метод для отображения категории рецепта в форме редактирования
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "recipe":
            kwargs["queryset"] = Recipe.objects.all().order_by('title')
            return super().formfield_for_foreignkey(db_field, request, **kwargs)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

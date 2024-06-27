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


class CategoryInline(admin.TabularInline):
    model = Ingredient.categories.through
    extra = 1


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "description", "image", "slug"]
    search_fields = ["name", "description"]
    list_filter = ["name", "description"]

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
    ]
    # Отображение "categories" через "through"
    inlines = (CategoryInline,)


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('u_name', 'u_anno')
    list_editable = ['u_anno', ]
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

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "recipe":
            kwargs["queryset"] = Recipe.objects.all().order_by('title')
            return super().formfield_for_foreignkey(db_field, request, **kwargs)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

# class RecipeIngredientInline(admin.TabularInline):
#     model = RecipeIngredient
#     extra = 1
#     fields = ['ingredient', 'unit']
#
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == 'ingredient':
#             kwargs['queryset'] = Ingredient.objects.all().order_by('name')
#         elif db_field.name == 'unit':
#             kwargs['queryset'] = Unit.objects.all().order_by('u_name')
#         return super().formfield_for_foreignkey(db_field, request, **kwargs)
#
# @admin.register(RecipeIngredient)
# class RecipeIngredientAdmin(admin.ModelAdmin):
#     list_display = ('recipe', 'register_date')
#     list_filter = ('recipe',)
#     search_fields = ('recipe__title', 'ingredient__name', 'unit__u_name')
#     fields = [
#         "recipe",
#     ]

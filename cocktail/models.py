from django.db import models as m
from django.urls import reverse


class Category(m.Model):
    name = m.CharField(max_length=150, unique=True, verbose_name='Название')
    description = m.TextField(blank=True, null=True, verbose_name='Описание')
    slug = m.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    def __str__(self):
        return f"Категория: {self.name}, Описание: {self.description} slug{self.slug}"

    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
        ordering = ("id",)


class Ingredient(m.Model):
    name = m.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = m.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = m.TextField(blank=True, null=True, verbose_name='Описание')
    image = m.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение')
    category = m.ForeignKey(to=Category, on_delete=m.CASCADE, verbose_name='Категория')

    def __str__(self):
        return f"{self.name}, цена: {self.description}"

    def get_absolute_url(self):
        return reverse("catalog:product", kwargs={"product_slug": self.slug})

    def display_id(self):
        return f"{self.id:05}"

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ("id",)


class Unit(m.Model):
    u_name = m.CharField(max_length=16, null=False, db_index=True, unique=True,
                         verbose_name='Обозначение единицы измерения')
    u_anno = m.CharField(max_length=128, null=False, verbose_name='Краткое описание')

    def __str__(self):
        return f'{self.u_anno} ({self.u_name})'

    class Meta:
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единицы измерения'


class Recipe(m.Model):
    title = m.CharField(max_length=128, unique=True, verbose_name='Название')
    slug = m.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = m.TextField(verbose_name='Описание')
    preparation_steps = m.TextField(verbose_name='Шаги приготовления')
    preparation_time = m.PositiveIntegerField(verbose_name='Время приготовления (в минутах)')
    image = m.ImageField(upload_to='recipe_images', blank=True, null=True, verbose_name='Изображение')
    author = m.CharField(max_length=128, verbose_name='Автор')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'


class RecipeIngredient(m.Model):
    recipe = m.ForeignKey(Recipe, on_delete=m.CASCADE, related_name='ingredients', verbose_name='Рецепт')
    ingredient = m.ForeignKey(Ingredient, on_delete=m.CASCADE, verbose_name='Ингредиент')
    unit = m.ForeignKey(Unit, on_delete=m.CASCADE, verbose_name='Единица измерения')
    register_date = m.DateField(auto_now_add=True, verbose_name='Дата создания рецепта')

    class Meta:
        verbose_name = 'Рецепт Коктейля'
        verbose_name_plural = 'Рецепты Коктейлей'

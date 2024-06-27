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

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ("id",)

    def get_absolute_url(self):
        return reverse("catalog:product", kwargs={"product_slug": self.slug})

    def display_id(self):
        return f"{self.id:05}"

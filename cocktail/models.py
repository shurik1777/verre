from django.db import models as m


class Category(m.Model):
    name = m.CharField(max_length=100)
    description = m.TextField(default='', blank=True)
    photo = m.ImageField(upload_to='category_photos', blank=True, null=True)

    def __str__(self):
        return f"Категория: {self.name}, Описание: {self.description}, Фото: {self.photo}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

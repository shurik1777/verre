# Generated by Django 5.0.6 on 2024-06-27 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocktail', '0003_alter_category_options_category_slug_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(db_index=True, max_length=16, unique=True, verbose_name='Обозначение единицы измерения')),
                ('u_anno', models.CharField(max_length=128, verbose_name='Краткое описание')),
            ],
            options={
                'verbose_name': 'Единица измерения',
                'verbose_name_plural': 'Единицы измерения',
            },
        ),
    ]

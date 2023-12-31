# Generated by Django 4.2.2 on 2023-06-14 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='image',
            field=models.ImageField(upload_to='hero/', verbose_name='Gambar'),
        ),
        migrations.AlterField(
            model_name='hero',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Judul'),
        ),
    ]

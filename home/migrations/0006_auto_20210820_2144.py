# Generated by Django 3.1.13 on 2021-08-21 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210820_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.CharField(max_length=400, null=True, verbose_name='Imagen'),
        ),
    ]

# Generated by Django 3.1.13 on 2021-08-21 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210820_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comprador',
            name='imagen',
            field=models.CharField(max_length=300, null=True, verbose_name='Foto'),
        ),
    ]
# Generated by Django 3.2 on 2021-04-27 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0004_auto_20210424_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

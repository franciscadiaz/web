# Generated by Django 3.2 on 2021-05-04 18:13

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0005_alter_anuncio_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='texto',
            field=ckeditor.fields.RichTextField(verbose_name='Contenido'),
        ),
    ]

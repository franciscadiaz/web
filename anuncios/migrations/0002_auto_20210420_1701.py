# Generated by Django 3.2 on 2021-04-20 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='anuncio',
            options={'ordering': ('-created',), 'verbose_name': 'Noticia', 'verbose_name_plural': 'Noticias'},
        ),
        migrations.AddField(
            model_name='anuncio',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Última edición'),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Creado'),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='texto',
            field=models.TextField(verbose_name='Contenido'),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='titulo',
            field=models.CharField(max_length=150, verbose_name='Título'),
        ),
    ]
# Generated by Django 3.1.13 on 2021-09-01 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0005_auto_20210901_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemonentity',
            name='attack',
            field=models.IntegerField(blank=True, null=True, verbose_name='атака'),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='defense',
            field=models.IntegerField(blank=True, null=True, verbose_name='защита'),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='health',
            field=models.IntegerField(blank=True, null=True, verbose_name='здоровье'),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='level',
            field=models.IntegerField(blank=True, null=True, verbose_name='уровень'),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='stamina',
            field=models.IntegerField(blank=True, null=True, verbose_name='выносливость'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='pokemons', verbose_name='картинка'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title',
            field=models.TextField(verbose_name='имя'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='lat',
            field=models.FloatField(verbose_name='широта'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='lon',
            field=models.FloatField(verbose_name='долгота'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='pokemon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon_entities.pokemon', verbose_name='покемон'),
        ),
    ]

# Generated by Django 3.1.13 on 2021-09-01 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0007_auto_20210901_1445'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='en_title',
            new_name='title_en',
        ),
        migrations.RenameField(
            model_name='pokemon',
            old_name='jp_title',
            new_name='title_jp',
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='photo',
            field=models.ImageField(blank=True, default='https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832&fill=transparent', upload_to='pokemons', verbose_name='картинка'),
        ),
    ]

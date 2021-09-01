from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.TextField(verbose_name='имя')
    photo = models.ImageField(verbose_name='картинка', upload_to="pokemons", null=True, blank=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, verbose_name='покемон', on_delete=models.CASCADE)

    lat = models.FloatField(verbose_name='широта')
    lon = models.FloatField(verbose_name='долгота')

    appeared_at = models.DateTimeField(verbose_name='появится', null=True, blank=True)
    disappeared_at = models.DateTimeField(verbose_name='исчезнет', null=True, blank=True)



from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.TextField()
    photo = models.ImageField(upload_to="pokemons", null=True, blank=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

    lat = models.FloatField()
    lon = models.FloatField()

    appeared_at = models.DateTimeField(verbose_name='появится', null=True, blank=True)
    disappeared_at = models.DateTimeField(verbose_name='исчезнет', null=True, blank=True)



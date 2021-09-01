from django.db import models  # noqa F401

DEFAULT_IMAGE_URL = (
    "https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision"
    "/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832"
    "&fill=transparent"
)

class Pokemon(models.Model):
    title = models.TextField(verbose_name="имя")
    photo = models.ImageField(
        verbose_name="картинка", upload_to="pokemons", blank=True, default=DEFAULT_IMAGE_URL,
    )
    en_title = models.CharField(verbose_name='имя на английском', max_length=200, blank=True)
    jp_title = models.CharField(verbose_name='имя на японском', max_length=200, blank=True)
    description = models.TextField(verbose_name='описание', blank=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon, verbose_name="покемон", on_delete=models.CASCADE
    )

    lat = models.FloatField(verbose_name="широта")
    lon = models.FloatField(verbose_name="долгота")

    appeared_at = models.DateTimeField(
        verbose_name="появится", null=True, blank=True
    )
    disappeared_at = models.DateTimeField(
        verbose_name="исчезнет", null=True, blank=True
    )

    level = models.IntegerField(verbose_name='уровень', null=True, blank=True)
    health = models.IntegerField(verbose_name='здоровье', null=True, blank=True)
    attack = models.IntegerField(verbose_name='атака', null=True, blank=True)
    defense = models.IntegerField(verbose_name='защита', null=True, blank=True)
    stamina = models.IntegerField(verbose_name='выносливость', null=True, blank=True)

    def __str__(self):
        return f"{self.pokemon.title}: {self.lat}, {self.lon}"

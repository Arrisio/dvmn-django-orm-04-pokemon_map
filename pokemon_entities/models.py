from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.TextField()
    photo = models.ImageField(upload_to='pokemons', null=True, blank=True)

    def __str__(self):
        return self.title
from django.db import models

# Create your models here.

class CountryData(models.Model):
    country = models.CharField(max_length=200)
    population = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Country Population Data'

    def __str__(self):
        return f'{self.country}-{self.population}'
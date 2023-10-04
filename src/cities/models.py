from django.db import models


class City(models.Model):
    name = models.CharField(max_length=70)

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"

    def __str__(self) -> str:
        return self.name

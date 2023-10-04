from django.db import models

from categories.models import Category
from cities.models import City


class Advert(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    views = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Advert"
        verbose_name_plural = "Adverts"

    def __str__(self) -> str:
        return self.title


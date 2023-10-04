from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=70)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name
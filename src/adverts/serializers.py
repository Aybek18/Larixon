from rest_framework import serializers

from adverts.models import Advert


class AdvertSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.name")
    city = serializers.CharField(source="city.name")

    class Meta:
        model = Advert
        fields = ("id", "created_at", "title", "description", "city", "category", "views")

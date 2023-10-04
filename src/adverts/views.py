from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from adverts.models import Advert
from adverts.serializers import AdvertSerializer


class AdvertListAPIView(ListAPIView):
    serializer_class = AdvertSerializer
    queryset = Advert.objects.select_related('city', 'category').all()


class AdvertRetrieveAPIView(RetrieveAPIView):
    serializer_class = AdvertSerializer
    queryset = Advert.objects.select_related('city', 'category').all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
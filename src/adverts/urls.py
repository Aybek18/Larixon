from django.urls import path

from adverts.views import AdvertListAPIView, AdvertRetrieveAPIView

urlpatterns = [
    path("", AdvertListAPIView.as_view(), name="advert-list"),
    path("<int:pk>/`", AdvertRetrieveAPIView.as_view(), name="advert-retrieve")
]

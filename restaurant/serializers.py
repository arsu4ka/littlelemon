from rest_framework.serializers import ModelSerializer
from . import models


class MenuItemSerializer(ModelSerializer):
    class Meta:
        model = models.MenuItem
        fields = "__all__"


class BookingSerializer(ModelSerializer):
    class Meta:
        model = models.Booking
        fields = "__all__"
        
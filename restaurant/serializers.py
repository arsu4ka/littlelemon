from rest_framework.serializers import ModelSerializer
from . import models


class MenuItemSerializer(ModelSerializer):
    class Meta:
        model = models.MenuItem
        fields = "__all__"

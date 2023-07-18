from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from . import models
from . import serializers


def index(request):
    return render(request, "index.html", {})


class MenuItemsView(generics.ListCreateAPIView):
    queryset = models.MenuItem.objects.all()
    serializer_class = serializers.MenuItemSerializer

    def get_permissions(self):
        permission_classes = []
        if self.request.method == "POST":
            permission_classes.append(permissions.IsAuthenticated)
        return [permission() for permission in permission_classes]


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.MenuItem.objects.all()
    serializer_class = serializers.MenuItemSerializer

    def get_permissions(self):
        permission_classes = []
        method = self.request.method
        if method == "DELETE" or method == "PUT" or method == "PATCH":
            permission_classes.append(permissions.IsAuthenticated)
        return [permission() for permission in permission_classes]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = models.Booking.objects.all()
    serializer_class = serializers.BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

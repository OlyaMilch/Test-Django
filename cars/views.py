from rest_framework import viewsets
from .models import Country, Manufacturer, Car, Comment
from .serializers import CountrySerializer, ManufacturerSerializer, CarSerializer, CommentSerializer
from rest_framework.permissions import AllowAny
from .permissions import IsAuthenticatedOrReadOnlyForUnsafe, CommentPermission
from rest_framework.viewsets import ModelViewSet


# ModelViewSet automatically creates all CRUD!

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticatedOrReadOnlyForUnsafe]  # Token for POST, PUT, DELETE


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    permission_classes = [IsAuthenticatedOrReadOnlyForUnsafe]


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticatedOrReadOnlyForUnsafe]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [CommentPermission]

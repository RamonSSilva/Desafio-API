from rest_framework.viewsets import ModelViewSet
from .models import Pet
from .serializers import PetSerializer


class PetViewSet(ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

from rest_framework.viewsets import ModelViewSet
from .models import Vacina
from .serializers import VacinaSerializer


class VacinaViewSet(ModelViewSet):
    queryset = Vacina.objects.all()
    serializer_class = VacinaSerializer

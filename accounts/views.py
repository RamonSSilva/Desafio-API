from rest_framework.viewsets import ModelViewSet
from .models import Responsavel
from .serializers import ResponsavelSerializer


class ResponsavelViewSet(ModelViewSet):
    queryset = Responsavel.objects.all()
    serializer_class = ResponsavelSerializer

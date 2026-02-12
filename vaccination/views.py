from rest_framework.viewsets import ModelViewSet
from .models import Vacinacao
from .serializers import VacinacaoSerializer


class VacinacaoViewSet(ModelViewSet):
    queryset = Vacinacao.objects.all()
    serializer_class = VacinacaoSerializer

from rest_framework.routers import DefaultRouter
from .views import VacinacaoViewSet

router = DefaultRouter()
router.register(r'vacinacoes', VacinacaoViewSet)

urlpatterns = router.urls

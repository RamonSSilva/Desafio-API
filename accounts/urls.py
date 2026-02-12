from rest_framework.routers import DefaultRouter
from .views import ResponsavelViewSet

router = DefaultRouter()
router.register(r'responsaveis', ResponsavelViewSet)

urlpatterns = router.urls

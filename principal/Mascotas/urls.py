from rest_framework.routers import DefaultRouter
from .views import MascotaViewSet

router = DefaultRouter()
router.register('mascotas', MascotaViewSet)
urlpatterns = router.urls
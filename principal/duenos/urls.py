from rest_framework.routers import DefaultRouter
from .views import DuenoViewSet

router = DefaultRouter()
router.register('duenos', DuenoViewSet)
urlpatterns = router.urls
from rest_framework import routers
from .views import ProjectViewSet

router = routers.DefaultRouter()

router.register(prefix='api/projects', viewset=ProjectViewSet, basename='projects')

urlpatterns = router.urls
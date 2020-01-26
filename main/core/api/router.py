from rest_framework import routers

from main.core.api.views.test import TestViewSet

router = routers.DefaultRouter()
router.register('tests', TestViewSet)

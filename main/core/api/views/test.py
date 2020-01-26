from rest_framework import viewsets

from main.core.api.serializers import TestSerializer
from main.core.models import Test


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

from rest_framework import serializers

from main.core.models import Test


class TestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Test
        fields = [
            'url', 'name'
        ]

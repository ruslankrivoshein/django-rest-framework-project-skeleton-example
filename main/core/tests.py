from django.test import Client, TestCase
from rest_framework.test import APIRequestFactory

from main.core.api.serializers import TestSerializer
from main.core.models import Test


class CoreModelsTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super(CoreModelsTests, cls).setUpClass()

        cls.test = Test.objects.create(name='Test №1')

    def test_simple_model_repr(self):
        self.assertEqual("Test(name='Test №1')", repr(self.test))

    def test_simple_model_str(self):
        self.assertEqual("Test №1", str(self.test))


class CoreSerializersTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super(CoreSerializersTests, cls).setUpClass()

        cls.factory = APIRequestFactory()

        cls.test = Test.objects.create(name='Test №1')

        cls.test_fields = {
            'name': 'Test №1'
        }

    def test_test_has_expected_fields(self):
        request = self.factory.get('/api/tests/')

        test_serializer = TestSerializer(instance=self.test,
                                         context={'request': request})

        fields = test_serializer.fields
        self.assertEqual(set(fields.keys()), {'url', 'name'})


class CoreViewsTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super(CoreViewsTests, cls).setUpClass()

        cls.test = Test.objects.create(id=1, name='Test №1')

    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = Client()

    def test_schema(self):
        expected = {
            'tests': 'http://testserver/api/tests/'
        }

        schema = self.client.get('/api/')
        self.assertEqual(schema.data, expected)

    def test_get_all_tests(self):
        request = self.factory.get('/tests/')

        expected = {
            'url': 'http://testserver/api/tests/1/',
            'name': 'Test №1'
        }

        serializer = TestSerializer(self.test, context={'request': request})
        self.assertEqual(serializer.data, expected)

from django.test import TestCase
from carambus_py.models_xxx import Account  # Import your models_xxx here


class BasicTest(TestCase):

    def setUp(self):
        # Set up data for the whole TestCase
        Account.objects.create(id="1", name="test")

    def test_model_data(self):
        # Test that the model data is created correctly
        item = Account.objects.get(id="1")
        self.assertEqual(item.name, "test")

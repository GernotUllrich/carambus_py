# your_project/tests/test_all_models.py
from django.test import TestCase
from carambus_py.tests.utils.models_import_helper import import_all_models


class TestAllModels(TestCase):
    def setUp(self):
        self.models = import_all_models()

    def test_models_exist(self):
        for model_label, model_class in self.models.items():
            with self.subTest(model=model_label):
                self.assertIsNotNone(model_class)
                # You can add more assertions to test model-specific behaviors

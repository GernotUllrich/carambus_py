from django.test import TestCase
from django.contrib.auth import get_user_model
from carambus_py.models_xxx import Account

User = get_user_model()


class AssociationTest(TestCase):

    def setUp(self):
        self.account = Account.objects.create(name="Example Account")
        self.user = User.objects.create(username="exampleuser", password="password", account=self.account)

    def test_account_has_many_users(self):
        # Assert that the user's account matches the created account
        self.assertEqual(self.user.account, self.account)
        # Assert the account's user set contains the created user
        self.assertIn(self.user, self.account.user_set.all())

    def test_user_belongs_to_account(self):
        # Assert that the user is associated with the account
        self.assertEqual(self.user.account, self.account)

    def tearDown(self):
        # Ensure cleanup to avoid test data pollution
        Account.objects.all().delete()
        User.objects.all().delete()

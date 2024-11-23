from django.test import TestCase

from django.db import IntegrityError


# Import all models
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import Permission
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.sessions.models import Session


class AssociationTests(TestCase):

    def test_logentry_user_foreign_key(self):
        """Test LogEntry.user ForeignKey to User"""
        try:
            obj = LogEntry.objects.create(user=User.objects.create())
            self.assertIsNotNone(obj.user)
        except IntegrityError:
            self.fail('LogEntry.user ForeignKey creation failed')


    def test_logentry_content_type_foreign_key(self):
        """Test LogEntry.content_type ForeignKey to ContentType"""
        try:
            obj = LogEntry.objects.create(content_type=ContentType.objects.create())
            self.assertIsNotNone(obj.content_type)
        except IntegrityError:
            self.fail('LogEntry.content_type ForeignKey creation failed')


    def test_permission_content_type_foreign_key(self):
        """Test Permission.content_type ForeignKey to ContentType"""
        try:
            obj = Permission.objects.create(content_type=ContentType.objects.create())
            self.assertIsNotNone(obj.content_type)
        except IntegrityError:
            self.fail('Permission.content_type ForeignKey creation failed')


    def test_group_permissions_many_to_many_field(self):
        """Test Group.permissions ManyToManyField to Permission"""
        try:
            obj = Group.objects.create()
            related_obj = Permission.objects.create()
            obj.permissions.add(related_obj)
            self.assertIn(related_obj, obj.permissions.all())
        except IntegrityError:
            self.fail('Group.permissions ManyToManyField creation failed')


    def test_user_groups_many_to_many_field(self):
        """Test User.groups ManyToManyField to Group"""
        try:
            obj = User.objects.create()
            related_obj = Group.objects.create()
            obj.groups.add(related_obj)
            self.assertIn(related_obj, obj.groups.all())
        except IntegrityError:
            self.fail('User.groups ManyToManyField creation failed')


    def test_user_user_permissions_many_to_many_field(self):
        """Test User.user_permissions ManyToManyField to Permission"""
        try:
            obj = User.objects.create()
            related_obj = Permission.objects.create()
            obj.user_permissions.add(related_obj)
            self.assertIn(related_obj, obj.user_permissions.all())
        except IntegrityError:
            self.fail('User.user_permissions ManyToManyField creation failed')


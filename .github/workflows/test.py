"""
Unit tests for views.
"""
from django.test import SimpleTestCase

from app import views

class ViewsTests(SimpleTestCase):

    def test_make_list_unique(self):
        """ Test making a list unique. """
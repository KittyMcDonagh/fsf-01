# TestCase is the base object that we will inherit from
from django.test import TestCase

# Create your tests here.

class TestDjango(TestCase):

# Tests must begin with "test_" otherwise Django wont find them
# Change test to make it pass.      
    def test_is_this_thing_on(self):
        self.assertEqual(1, 0)
# TestCase is the base object that we will inherit from
from django.test import TestCase
from .forms import ItemForm

# Create your tests here.

class TestToDoItemForm(TestCase):

# Test that it's possible to create a form with just a name
    def test_can_create_an_item_with_just_a_name(self):
        form = ItemForm({ 'name': "Create Tests"})
        self.assertTrue(form.is_valid())
        
    # Test get the correct message if no name given
    def test_correct_message_for_missing_name(self):
        form = ItemForm({ 'name': ""})
        
    # This that the form is deemed invalid
        self.assertFalse(form.is_valid())
        
    # Test that this message is returned
        self.assertEqual(form.errors['name'], [u'This field is required.'])
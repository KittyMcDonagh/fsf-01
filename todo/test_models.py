# TestCase is the base object that we will inherit from
from django.test import TestCase
from .models import Item

class TestItemModel(TestCase):
    
    # Test that 'done' defaults to False
    def test_done_defaults_to_False(self):
        item = Item(name='Create a Test')
        item.save()
        
        self.assertEqual(item.name, 'Create a Test')
        
    # The following 2 ways of checking for False will have the same result
        self.assertFalse(item.done)
        self.assertEqual(item.done, False)
        
    
    # Test that an item with name and status can be created    
    def test_can_create_an_item_with_a_name_and_status(self):
        item = Item(name='Create a Test', done=True)
        item.save()
        
        self.assertEqual(item.name, 'Create a Test')
        self.assertTrue(item.done)
    
    # Test that models.py is correctly returning the name entered as a string
    def test_item_as_a_string(self):
        item = Item(name="Create a Test")
        self.assertEqual("Create a Test", str(item))
        
         
        
        
        
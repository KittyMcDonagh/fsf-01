# TestCase is the base object that we will inherit from
from django.test import TestCase
from django.shortcuts import get_object_or_404

from .models import Item


class TestViews(TestCase):
    
    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "todo_list.html")
        
    
    def test_get_add_item_page(self):
        page = self.client.get("/add")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "item_form.html")
        
        
    def test_get_edit_item_page(self):
        
    # Create a dummy entry in alias db and save it. 
    # Django will create an id for it
        item = Item(name = 'Create a test')
        item.save()
        
        # Get the page "/edit/id of dummy item"
        page = self.client.get("/edit/{0}".format(item.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "item_form.html")
        
    # Since we havent created anything in the database, this will throw a 404
    # The .get" is same as "get_object_or_404(Item, pk=id)". If it cant find
    # the object it will throw a 404.
    def test_get_edit_page_for_item_that_does_not_exist(self):
        page = self.client.get("/edit/1")
        self.assertEqual(page.status_code, 404)
    
    # Test 'add_an_item'
    def test_post_create_an_item(self):
        response = self.client.post("/add", {'name': "Create a Test"})
        item = get_object_or_404(Item, pk=1)
        self.assertEqual(item.done, False)
    
    # Test 'edit_an_item'
    def test_post_edit_an_item(self):
        
    # First create an item and save it to the db
        item = Item(name="Create a Test")
        item.save()
    
    # The item id which is automatically assigned by Django
        id = item.id
        
    # Edit the item's name
        response = self.client.post("/edit/{0}".format(id), {'name': 'A different name'})
        
    # Get the item from the database and confirm the name has changed
        item = get_object_or_404(Item, pk=id)
        self.assertEqual(item.name, 'A different name')
        
        
        
    # Test 'toggle_an_item'
    def test_toggle_status(self):
        
    # First create an item and save it to the db
        item = Item(name="Create a Test")
        item.save()
    
    # The item id which is automatically assigned by Django
        id = item.id
        
    # Post to the /toggle - as this item was created with no done status, it 
    # was automatically set to False. The toggle will flip it to True
        response = self.client.post("/toggle/{0}".format(id))
        
    # Get the item from the database and confirm the name has changed
        item = get_object_or_404(Item, pk=id)
        self.assertEqual(item.done, True)
        
        
        


        
        
        
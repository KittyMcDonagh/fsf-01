from django import forms

# See class Item in models.py - this is imported here
from .models import Item

# Create a form based on forms.ModelForm (see imported forms above)
class ItemForm(forms.ModelForm):
    # This inner class tell django what we want; form to be based on Item model
    # and the fields we want are the name and done fields
    class Meta:
        model = Item
        fields = ("name", "done")
    
    
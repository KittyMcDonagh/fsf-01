from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Item

# Import ItemForm (class = ItemForm created in forms.py)
from .forms import ItemForm


# todo_list view
def get_todo_list(request):
    results=Item.objects.all()
    return render(request, "todo_list.html", {'items': results})

# Add an item to the to do list
def create_an_item(request):
    if request.method=="POST":
        
        # ItemForm imported above (class = ItemForm created in forms.py)
        # POST  is to populate it with the fields we get from the POST in a 
        # request object, and FILES is used if there are files to be uploaded
        
        form = ItemForm(request.POST, request.FILES)
        
        # cause django to validate the form
        if form.is_valid():
            form.save()
            return redirect(get_todo_list)
    
    # if it's not a POST request, return an empty form
    
    else:
        form=ItemForm()
       
    return render(request, "item_form.html", {'form': form})

# Edit a specific item    
def edit_an_item(request, id):
    
# Get the item we just clicked on
    item = get_object_or_404(Item, pk=id)
    
    # If this is the update from item_form.html, save the update
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(get_todo_list)
    
    else:
        # Display the item that is to be edited
        # Create a form and pass in "item" as the instance that we want to construct 
        # the object from 
        form = ItemForm(instance=item)
    
    return render(request, "item_form.html", {'form': form})
    
    
# Toggle the done status. This will save the setting and reloa the todo_list
def toggle_status(request, id):
     
    # Get the item whose done flag was clicked
    item = get_object_or_404(Item, pk=id)
     
    # Reverse the setting of the done flag, if done make it not done, if 
    # not done make it done
    item.done = not item.done
    item.save()
     
    return redirect(get_todo_list)
     
     
    
    
    
    
    
    
    
    
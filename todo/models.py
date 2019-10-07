from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=30, blank=False)
    done = models.BooleanField(blank=False, default=False)
    
# The item list description shows "Item object" for all items. By adding the 
# following code, the list will show the actual Item description input by the 
# user, e.g. "Plan Pproject", "Launch Project"
    def __str__(self):
        return self.name
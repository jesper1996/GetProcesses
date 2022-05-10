from django.contrib import admin
from .models import ToDoList, Item
# Adding models to the admin page.
admin.site.register(ToDoList)
admin.site.register(Item)
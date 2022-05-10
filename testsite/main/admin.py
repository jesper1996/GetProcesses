from django.contrib import admin
from .models import ToDoList, Item, Processes


admin.site.site_header = 'Processes'
# Adding models to the admin page.
admin.site.register(ToDoList)
admin.site.register(Item)
admin.site.register(Processes)


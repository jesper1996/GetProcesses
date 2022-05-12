from django.contrib import admin
from .models import Processes
from django.contrib.auth.models import Group, User

admin.site.site_header = 'Processes'

# Adding and removing models to the admin page.
admin.site.register(Processes)
admin.site.unregister(Group)
admin.site.unregister(User)
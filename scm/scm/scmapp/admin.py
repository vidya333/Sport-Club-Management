from django.contrib import admin

from .models import User,Book_ground,Admin,Event
admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Book_ground)
admin.site.register(Event)
from django.contrib import admin

# Register your models here.
from .models import reservation, contact, image
admin.site.register(reservation)
admin.site.register(contact)
admin.site.register(image)
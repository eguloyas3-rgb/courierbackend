from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Track)
admin.site.register(TrackingPackage)
admin.site.register(Label)
admin.site.register(Complaint)
admin.site.register(ContactMessage)
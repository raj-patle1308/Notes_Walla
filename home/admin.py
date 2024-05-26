from django.contrib import admin
from home.models import Contact
# Register your models here.

admin.site.register(Contact)

from django.contrib import admin
from .models import PublicNotes

admin.site.register(PublicNotes)
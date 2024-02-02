from django.contrib import admin
from .models import *

class FeedAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(feed, FeedAdmin)


# Register your models here.

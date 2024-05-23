from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(post, PostAdmin)
admin.site.register(postCategory)
admin.site.register(faq)
admin.site.register(docs)
admin.site.register(docsType)
admin.site.register(docsInPost)
admin.site.register(postContent)
admin.site.register(postContentType)
admin.site.register(products)
admin.site.register(dataFromForms)


# Register your models here.

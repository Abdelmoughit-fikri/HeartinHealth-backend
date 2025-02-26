from django.contrib import admin

from .models import Article,SecondaryImage,AttachedFile

admin.site.register(Article)
admin.site.register(SecondaryImage)
admin.site.register(AttachedFile)
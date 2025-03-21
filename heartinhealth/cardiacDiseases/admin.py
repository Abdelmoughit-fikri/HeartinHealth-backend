from django.contrib import admin
from .models import CdArticle, AttachedFile


class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "sub_category",
        "primary_image",
        'is_highlighted',
        'is_important',
        "created_at",
        "updated_at",
    )

class CDAttachedFileAdmin(admin.ModelAdmin):
    list_display = (
        'attached_file',
    )

admin.site.register(CdArticle, ArticleAdmin)
admin.site.register(AttachedFile,CDAttachedFileAdmin)

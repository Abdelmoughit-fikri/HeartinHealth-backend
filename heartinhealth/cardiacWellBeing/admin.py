from django.contrib import admin
from .models import CwbArticle, AttachedFile


class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "primary_image",
        "is_active",
        'is_highlighted',
        'is_important',
        "created_at",
        "updated_at",
    )
    
class CWBttachedFileAdmin(admin.ModelAdmin):
    list_display = (
        'attached_file',
    )


admin.site.register(CwbArticle, ArticleAdmin)
admin.site.register(AttachedFile,CWBttachedFileAdmin)

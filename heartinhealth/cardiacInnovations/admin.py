from django.contrib import admin
from .models import CiArticle, AttachedFile


class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "primary_image",
        'is_highlighted',
        "is_important",
        "created_at",
        "updated_at"
    )
    
class CIAttachedFileAdmin(admin.ModelAdmin):
    list_display = (
        'attached_file',
    )


admin.site.register(CiArticle, ArticleAdmin)
admin.site.register(AttachedFile,CIAttachedFileAdmin)

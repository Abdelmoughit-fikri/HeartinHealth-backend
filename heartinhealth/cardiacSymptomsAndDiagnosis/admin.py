from django.contrib import admin
from .models import CsdArticle, AttachedFile


class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "sub_category",
        "primary_image",
        "is_active",
        'is_highlighted',
        'is_important',
        "created_at",
        "updated_at",
    )

class SDAttachedFileAdmin(admin.ModelAdmin):
    list_display = (
        'attached_file',
    )


admin.site.register(CsdArticle, ArticleAdmin)
admin.site.register(AttachedFile,SDAttachedFileAdmin)

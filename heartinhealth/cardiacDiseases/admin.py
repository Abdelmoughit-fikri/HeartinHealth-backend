from django.contrib import admin
from django.contrib.auth.models import User
from .models import Article, SecondaryImage, AttachedFile


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_author_full_name', 'category','primary_image', 'created_at')

    def get_author_full_name(self, obj):
        if obj.author:
            full_name = f"{obj.author.first_name} {obj.author.last_name}".strip()
            return full_name if full_name else obj.author.username
        return "No Author"

    get_author_full_name.short_description = "Author"

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "author":
            kwargs["queryset"] = User.objects.filter(
                id=request.user.id)  # Show only the logged-in user
            kwargs["initial"] = request.user  # Preselect the logged-in user
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Article, ArticleAdmin)
admin.site.register(SecondaryImage)
admin.site.register(AttachedFile)

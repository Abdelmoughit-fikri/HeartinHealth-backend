from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from .models import CwbArticle, SecondaryImage, AttachedFile


class CWBSecondaryImagesSRZ(serializers.ModelSerializer):
    class Meta:
        model = SecondaryImage
        fields = "__all__"


class CWBAttachedFilesSRZ(serializers.ModelSerializer):
    class Meta:
        model = AttachedFile
        fields = "__all__"


class CardiacWellBeingSRZ(serializers.ModelSerializer):
    secondary_images = CWBSecondaryImagesSRZ(many=True, read_only=True)
    attached_files = CWBAttachedFilesSRZ(many=True, read_only=True)
    author_full_name = serializers.SerializerMethodField()

    class Meta:
        model = CwbArticle
        fields = [
            "id",
            "title",
            "author_full_name",
            "author_label",
            "category",
            "overView",
            "content",
            "keywords",
            "created_at",
            "updated_at",
            "primary_image",
            "video_URL",
            "links",
            "is_active",
            "is_important",
            "is_highlighted",
            "is_highlighted_score",
            "attached_files",
            "secondary_images",
        ]
    @extend_schema_field(serializers.CharField(allow_null=True))  # Fix drf-spectacular warning
    def get_author_full_name(self, obj):
        if obj.author:
            full_name = f"{obj.author.first_name} {obj.author.last_name}".strip()
            return full_name if full_name else obj.author.username
        return None  # In case there's no author

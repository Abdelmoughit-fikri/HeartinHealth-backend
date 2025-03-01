from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from .models import CdArticle, SecondaryImage, AttachedFile


class CDSecondaryImagesSRZ(serializers.ModelSerializer):
    class Meta:
        model = SecondaryImage
        fields = "__all__"


class CDAttachedFilesSRZ(serializers.ModelSerializer):
    class Meta:
        model = AttachedFile
        fields = "__all__"


class CardiacDiseasesSRZ(serializers.ModelSerializer):
    secondary_images = CDSecondaryImagesSRZ(many=True, read_only=True)
    attached_files = CDAttachedFilesSRZ(many=True, read_only=True)
    author_full_name = serializers.SerializerMethodField()

    class Meta:
        model = CdArticle
        fields = [
            "id",
            "title",
            "author_full_name",
            "author_label",
            "category",
            "sub_category",
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
    def get_author_full_name(self, obj) -> str | None:
        if obj.author:
            full_name = f"{obj.author.first_name} {obj.author.last_name}".strip()
            return full_name if full_name else obj.author.username
        return None  # Consistent return type

from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from .models import CwbArticle, AttachedFile



class CWBAttachedFilesSRZ(serializers.ModelSerializer):
    class Meta:
        model = AttachedFile
        fields = "__all__"


class CardiacWellBeingSRZ(serializers.ModelSerializer):
    attached_files = CWBAttachedFilesSRZ(many=True, read_only=True)

    class Meta:
        model = CwbArticle
        fields = [
            "id",
            "title",
            "category",
            "description",
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
            "attached_files",
        ]

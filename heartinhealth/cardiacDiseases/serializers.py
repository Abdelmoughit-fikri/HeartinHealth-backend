from rest_framework import serializers
from .models import CdArticle, AttachedFile



class CDAttachedFilesSRZ(serializers.ModelSerializer):
    class Meta:
        model = AttachedFile
        fields = "__all__"


class CardiacDiseasesSRZ(serializers.ModelSerializer):
    attached_files = CDAttachedFilesSRZ(many=True, read_only=True)

    class Meta:
        model = CdArticle
        fields = [
            "id",
            "title",
            "category",
            "sub_category",
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


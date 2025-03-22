from rest_framework import serializers
from .models import CiArticle, AttachedFile



class CIAttachedFilesSRZ(serializers.ModelSerializer):
    class Meta:
        model = AttachedFile
        fields = "__all__"


class CardiacInnovationsSRZ(serializers.ModelSerializer):
    attached_files = CIAttachedFilesSRZ(many=True, read_only=True)

    class Meta:
        model = CiArticle
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
            "attached_files",
        ]

from rest_framework import serializers
from .models import CsdArticle, AttachedFile



class CSDAttachedFilesSRZ(serializers.ModelSerializer):
    class Meta:
        model = AttachedFile
        fields = "__all__"


class CardiacSymptomsAndDiagnosisSRZ(serializers.ModelSerializer):
    attached_files = CSDAttachedFilesSRZ(many=True, read_only=True)

    class Meta:
        model = CsdArticle
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
            "attached_files",
        ]


from rest_framework import serializers
from .models import CsdArticle, SecondaryImage, AttachedFile
from drf_spectacular.utils import extend_schema_field



class CSDSecondaryImagesSRZ(serializers.ModelSerializer):
    class Meta:
        model = SecondaryImage
        fields = "__all__"


class CSDAttachedFilesSRZ(serializers.ModelSerializer):
    class Meta:
        model = AttachedFile
        fields = "__all__"


class CardiacSymptomsAndDiagnosisSRZ(serializers.ModelSerializer):
    secondary_images = CSDSecondaryImagesSRZ(many=True, read_only=True)
    attached_files = CSDAttachedFilesSRZ(many=True, read_only=True)
    author_full_name = serializers.SerializerMethodField()

    class Meta:
        model = CsdArticle
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
    def get_author_full_name(self, obj):
        if obj.author:
            full_name = f"{obj.author.first_name} {obj.author.last_name}".strip()
            return full_name if full_name else obj.author.username
        return None  # In case there's no author

from rest_framework import serializers
from .models import Article, SecondaryImage, AttachedFile

class SecondaryImagesSRZ(serializers.ModelSerializer):
    class Meta:
        model = SecondaryImage
        fields = '__all__'

class AttachedFilesSRZ(serializers.ModelSerializer):
    class Meta:
        model = AttachedFile
        fields = '__all__'

class CardiacInnovationsSRZ(serializers.ModelSerializer):
    secondary_images = SecondaryImagesSRZ(many=True, read_only=True)
    attached_files = AttachedFilesSRZ(many=True, read_only=True)
    author_full_name = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = [
            'id', 'title', 'author_full_name', 'category',
            'overView', 'content', 'keywords', 'created_at', 'updated_at',
            'primary_image', 'video_URL', 'is_active', 'is_important',
            'is_highlighted', 'is_highlighted_score', 'attached_files', 'secondary_images'
        ]

    def get_author_full_name(self, obj):
        if obj.author:
            full_name = f"{obj.author.first_name} {obj.author.last_name}".strip()
            return full_name if full_name else obj.author.username
        return None  # In case there's no author

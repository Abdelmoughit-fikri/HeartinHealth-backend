from rest_framework import serializers
from .models import Article,SecondaryImage,AttachedFile

class SecondaryImagesSRZ(serializers.ModelSerializer):
    class Meta:
        model = SecondaryImage
        fields = '__all__'
class AttachedFilesSRZ(serializers.ModelSerializer):
    class Meta:
        model = AttachedFile
        fields = '__all__'
class CwbSRZ(serializers.ModelSerializer):
    secondary_images = SecondaryImagesSRZ(many=True, read_only=True)
    attached_files = AttachedFilesSRZ(many=True,read_only=True)
    class Meta:
        model = Article
        fields = '__all__'
        
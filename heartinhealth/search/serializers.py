from rest_framework import serializers
from cardiacDiseases.models import CdArticle
from cardiacInnovations.models import CiArticle
from cardiacSymptomsAndDiagnosis.models import CsdArticle
from cardiacWellBeing.models import CwbArticle


class CdSearchSRZ(serializers.ModelSerializer):
    author_full_name = serializers.SerializerMethodField()

    class Meta:
        model = CdArticle
        fields = [
            "id",
            "title",
            "author_full_name",
            "author_label",
            "category",
            "keywords",
            "created_at",
            "updated_at",
            "primary_image",
        ]

    def get_author_full_name(self, obj):
        if obj.author:
            return f"{obj.author.first_name} {obj.author.last_name}".strip()
        return "Unknown"


class CiSearchSRZ(serializers.ModelSerializer):
    author_full_name = serializers.SerializerMethodField()

    class Meta:
        model = CiArticle
        fields = [
            "id",
            "title",
            "author_full_name",
            "author_label",
            "category",
            "keywords",
            "created_at",
            "updated_at",
            "primary_image",
        ]

    def get_author_full_name(self, obj):
        if obj.author:
            return f"{obj.author.first_name} {obj.author.last_name}".strip()
        return "Unknown"


class CsdSearchSRZ(serializers.ModelSerializer):
    author_full_name = serializers.SerializerMethodField()

    class Meta:
        model = CsdArticle
        fields = [
            "id",
            "title",
            "author_full_name",
            "author_label",
            "category",
            "keywords",
            "created_at",
            "updated_at",
            "primary_image",
        ]

    def get_author_full_name(self, obj):
        if obj.author:
            return f"{obj.author.first_name} {obj.author.last_name}".strip()
        return "Unknown"


class CwbSearchSRZ(serializers.ModelSerializer):
    author_full_name = serializers.SerializerMethodField()

    class Meta:
        model = CwbArticle
        fields = [
            "id",
            "title",
            "author_full_name",
            "author_label",
            "category",
            "keywords",
            "created_at",
            "updated_at",
            "primary_image",
        ]

    def get_author_full_name(self, obj):
        if obj.author:
            return f"{obj.author.first_name} {obj.author.last_name}".strip()
        return "Unknown"

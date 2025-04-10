from rest_framework import serializers
from cardiacDiseases.models import CdArticle
from cardiacInnovations.models import CiArticle
from cardiacSymptomsAndDiagnosis.models import CsdArticle
from cardiacWellBeing.models import CwbArticle


class CdSearchSRZ(serializers.ModelSerializer):
    class Meta:
        model = CdArticle
        fields = [
            "id",
            "title",
            "category",
            "sub_category",
            "description",
            "keywords",
            "is_highlighted",
            "created_at",
            "updated_at",
            "primary_image",
        ]


class CiSearchSRZ(serializers.ModelSerializer):
    class Meta:
        model = CiArticle
        fields = [
            "id",
            "title",
            "category",
            "description",
            "keywords",
            "is_highlighted",
            "created_at",
            "updated_at",
            "primary_image",
        ]


class CsdSearchSRZ(serializers.ModelSerializer):
    class Meta:
        model = CsdArticle
        fields = [
            "id",
            "title",
            "category",
            "sub_category",
            "description",
            "keywords",
            "is_highlighted",
            "created_at",
            "updated_at",
            "primary_image",
        ]


class CwbSearchSRZ(serializers.ModelSerializer):
    class Meta:
        model = CwbArticle
        fields = [
            "id",
            "title",
            "category",
            "description",
            "keywords",
            "is_highlighted",
            "created_at",
            "updated_at",
            "primary_image",
        ]

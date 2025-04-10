from uuid import uuid4
from django.conf import settings
import boto3
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.response import Response
from .models import CdArticle
from .serializers import CardiacDiseasesSRZ
from rest_framework.pagination import PageNumberPagination
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework_api_key.permissions import HasAPIKey


class ArticlePagination(PageNumberPagination):
    page_size = 9
    page_size_query_param = "page_size"
    max_page_size = 30

    def get_paginated_response(self, data):
        return Response(
            {
                "count": self.page.paginator.count,
                "articles": data,
                "next": self.get_next_link(),
                "previous": self.get_previous_link(),
            }
        )


class CardiacDiseasesViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [HasAPIKey]
    queryset = CdArticle.objects.all()
    serializer_class = CardiacDiseasesSRZ
    pagination_class = ArticlePagination

    # my qery params are:
    # category | sub_category | latest | oldest | importance

    def get_queryset(self):
        queryset = CdArticle.objects.all().filter(is_active=True).order_by("-created_at")
        category = self.request.GET.get("category", None)
        sub_category = self.request.GET.get("sub_category", None)
        latest = self.request.GET.get("latest", None)
        oldest = self.request.GET.get("oldest", None)
        importance = self.request.GET.get("importance", None)
        highlighted = self.request.GET.get("highlighted", None)
        if category:
            queryset = queryset.filter(category__iexact=category)
        if sub_category:
            queryset = queryset.filter(sub_category__iexact=sub_category)
        if latest:
            queryset = queryset.order_by("-created_at")
        if oldest:
            queryset = queryset.order_by("created_at")
        if importance:
            queryset = queryset.filter(is_important=True)
        if highlighted:
            queryset = queryset.filter(is_highlighted=True)

        return queryset

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="category", type=str, description="Filter by category"
            ),
            OpenApiParameter(
                name="sub_category", type=str, description="Filter by sub_category"
            ),
            OpenApiParameter(
                name="latest", type=bool, description="Sort by latest (true/false)"
            ),
            OpenApiParameter(
                name="oldest", type=bool, description="Sort by oldest (true/false)"
            ),
            OpenApiParameter(
                name="importance",
                type=bool,
                description="order by article's importance (true/false)",
            ), OpenApiParameter(
                name='highlighted',
                type=bool,
                description='highlighted articles',
            ),
        ]
    )
    def list(self, request):
        """List articles with filters and pagination"""
        return super().list(request)



def upload_image(request):
    if request.method == 'POST' and request.FILES.get('upload'):
        file = request.FILES['upload']
        # Define the S3 folder path within the bucket
        folder_path = 'article_images/'  # Folder structure
        # Generate a unique file name
        file_name = f"{folder_path}{uuid4()}_{file.name}"
        
        # Upload the file to AWS S3
        s3 = boto3.client('s3', 
                         aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                         aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                         region_name='your-region')  # Replace with your S3 region
        
        try:
            s3.upload_fileobj(file, settings.AWS_STORAGE_BUCKET_NAME, file_name, 
                              ExtraArgs={'ContentType': file.content_type})
            
            # Generate the file URL
            file_url = f"https://{settings.AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/{file_name}"
            return JsonResponse({'url': file_url})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'No file uploaded'}, status=400)

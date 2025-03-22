from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import CwbArticle
from .serializers import CardiacWellBeingSRZ
from rest_framework.pagination import PageNumberPagination
from drf_spectacular.utils import extend_schema, OpenApiParameter


class ArticlePagination(PageNumberPagination):
    page_size = 7
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


class CardiacWellBeingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CwbArticle.objects.all()
    serializer_class = CardiacWellBeingSRZ
    pagination_class = ArticlePagination

    # my qery params are:
    # category | sub_category | latest

    def get_queryset(self):
        queryset = CwbArticle.objects.all().filter(is_active=True).order_by("-created_at")
        category = self.request.GET.get("category", None)
        latest = self.request.GET.get("latest", None)
        oldest = self.request.GET.get("oldest", None)
        importance = self.request.GET.get("importance", None)
        highlighted = self.request.GET.get("highlighted",None)
        if category:
            queryset = queryset.filter(category__iexact=category)
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
                name="latest", type=bool, description="Sort by latest (true/false)"
            ),
            OpenApiParameter(
                name="oldest", type=bool, description="Sort by oldest (true/false)"
            ),
            OpenApiParameter(
                name="importance",
                type=bool,
                description="order by article's importance (true/false)",
            ),OpenApiParameter(
                name='highlighted',
                type=bool,
                description='highlighted articles',
            ),
        ]
    )
    def list(self, request):
        """List articles with filters and pagination"""
        return super().list(request)

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Article
from .serializers import CwbSRZ
from rest_framework.pagination import PageNumberPagination


class ArticlePagination(PageNumberPagination):
    page_size = 7
    page_size_query_param = 'page_size'
    max_page_size = 30
    
    def get_paginated_response(self, data):
        return Response({
            "count": self.page.paginator.count,
            "articles": data,
            "next": self.get_next_link(),
            "previous": self.get_previous_link()
        })


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    serializer_class = CwbSRZ
    pagination_class = ArticlePagination

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.db.models import Q, Value
from django.db.models.functions import Concat
from cardiacDiseases.models import CdArticle
from cardiacInnovations.models import CiArticle
from cardiacSymptomsAndDiagnosis.models import CsdArticle
from cardiacWellBeing.models import CwbArticle
from .serializers import CdSearchSRZ, CiSearchSRZ, CsdSearchSRZ, CwbSearchSRZ
from drf_spectacular.utils import extend_schema


class searcHinhViewSet(ViewSet):
    @extend_schema(
        parameters=[],
        responses={
            200: {
                "search_results": CdSearchSRZ(many=True)  # Pick one for documentation
            }
        },
    )
    def list(self, request):
        query = self.request.GET.get("q", "")

        if not query:
            return Response({"error": "no search query provided"}, status=400)
        results = []
        CD_results = CdArticle.objects.annotate(
            author_full_name=Concat(
                "author__first_name", Value(" "), "author__last_name"
            )
        ).filter(
            Q(title__icontains=query)
            | Q(search_queries__icontains=query)
            | Q(author__first_name__icontains=query)
            | Q(author__last_name__icontains=query)
            | Q(author_full_name__icontains=query)
            | Q(category__icontains=query)
            | Q(sub_category__icontains=query)
        )
        results += CdSearchSRZ(CD_results, many=True).data
        ###
        CI_results = CiArticle.objects.annotate(
            author_full_name=Concat(
                "author__first_name", Value(" "), "author__last_name"
            )
        ).filter(
            Q(title__icontains=query)
            | Q(search_queries__icontains=query)
            | Q(author__first_name__icontains=query)
            | Q(author__last_name__icontains=query)
            | Q(author_full_name__icontains=query)
            | Q(author_label__icontains=query)
            | Q(category__icontains=query)
        )
        results += CiSearchSRZ(CI_results, many=True).data
        ###
        CSD_results = CsdArticle.objects.annotate(
            author_full_name=Concat(
                "author__first_name", Value(" "), "author__last_name"
            )
        ).filter(
            Q(title__icontains=query)
            | Q(search_queries__icontains=query)
            | Q(author__first_name__icontains=query)
            | Q(author__last_name__icontains=query)
            | Q(author_full_name__icontains=query)
            | Q(author_label__icontains=query)
            | Q(category__icontains=query)
            | Q(sub_category__icontains=query)
        )
        results += CsdSearchSRZ(CSD_results, many=True).data
        ###
        CWB_results = CwbArticle.objects.annotate(
            author_full_name=Concat(
                "author__first_name", Value(" "), "author__last_name"
            )
        ).filter(
            Q(title__icontains=query)
            | Q(title__icontains=query)
            | Q(author__first_name__icontains=query)
            | Q(author__last_name__icontains=query)
            | Q(author_full_name__icontains=query)
            | Q(author_label__icontains=query)
            | Q(category__icontains=query)
        )
        results += CwbSearchSRZ(CWB_results, many=True).data
        return Response({"search_results": results})

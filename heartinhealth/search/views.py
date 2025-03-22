from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from django.db.models import Q
from django.db.models.functions import Concat
from cardiacDiseases.models import CdArticle
from cardiacInnovations.models import CiArticle
from cardiacSymptomsAndDiagnosis.models import CsdArticle
from cardiacWellBeing.models import CwbArticle
from .serializers import CdSearchSRZ, CiSearchSRZ, CsdSearchSRZ, CwbSearchSRZ


class searcHinhViewSet(GenericViewSet):
    def list(self, request):
        query = self.request.GET.get("term", "")

        if not query:
            return Response({"error": "no search query provided"}, status=400)
        results = []
        CD_results = CdArticle.objects.filter(
            Q(title__icontains=query)
            | Q(search_queries__icontains=query)
            | Q(category__icontains=query)
            | Q(sub_category__icontains=query)
        )
        results += CdSearchSRZ(CD_results, many=True).data
        ###
        CI_results = CiArticle.objects.filter(
            Q(title__icontains=query)
            | Q(search_queries__icontains=query)
            | Q(category__icontains=query)
        )
        results += CiSearchSRZ(CI_results, many=True).data
        ###
        CSD_results = CsdArticle.objects.filter(
            Q(title__icontains=query)
            | Q(search_queries__icontains=query)
            | Q(category__icontains=query)
            | Q(sub_category__icontains=query)
        )
        results += CsdSearchSRZ(CSD_results, many=True).data
        ###
        CWB_results = CwbArticle.objects.filter(
            Q(title__icontains=query)
            | Q(search_queries__icontains=query)
            | Q(category__icontains=query)
        )
        results += CwbSearchSRZ(CWB_results, many=True).data
        return Response({"search_results": results})

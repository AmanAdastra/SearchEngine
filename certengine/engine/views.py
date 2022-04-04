from engine.models import Car
from rest_framework.generics import ListAPIView
from engine.serializers import CarSerializer
from engine.documents import CarDocument
from django.http import JsonResponse
from elasticsearch_dsl import Q
# Create your views here.


class CarList(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


def home_view(request):
    queryset = CarDocument.search().query("match_all")
    count = queryset.count()
    queryset = queryset[0:count].execute()
    serializer = CarSerializer(queryset, many=True)
    return JsonResponse(status=200, data=serializer.data, safe=False)
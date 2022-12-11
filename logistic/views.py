from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # при необходимости добавьте параметры фильтрации
    filter_backends = [SearchFilter]
    search_fileds = ['title', 'description']


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # при необходимости добавьте параметры фильтрации
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['address', 'products']


@api_view(['GET'])
def sample_view(request):
    return Response('Hello world!')

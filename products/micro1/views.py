from django.contrib.auth.models import Permission
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from micro1.serializers import DistributorSerializer, ProductSerializer
from .models import *

class ProductViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):

        print('sobreescribiendo LIST ')
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        print('update')
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        print("patch!!!!!!!!!!!!1")
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)




    def retrieve(self, request, pk=None):
        print('retrieve Product')
        diccionario = request.query_params.dict()
        if len(diccionario) == 2: 
            product_name = diccionario['producto']
            product_qt = diccionario['cantidad']
            product = Product.objects.get(product_name=product_name)
            print(product)
            print(product.product_qt)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        elif len(diccionario) == 1: 
            product_name = diccionario['producto']
            product = Product.objects.get(product_name=product_name)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
class DistributorViewSet(viewsets.ModelViewSet):
    queryset = Distributor.objects.all()
    serializer_class = DistributorSerializer

from email.policy import HTTP
from telnetlib import STATUS
from django.contrib.auth.models import Permission
from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets, renderers
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
import json

# Create your views here.
# ModelViewSet proporciona todos los metodos
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)   # model --> python 


    def retrieve(self, request, pk=None):
        diccionario = request.query_params.dict()
        len(diccionario)
        name = diccionario['name']
        password = diccionario['password']
        queryset = User.objects.all()
        if len(diccionario) == 2:
            user = get_object_or_404(queryset, name=name, password=password)
        elif len(diccionario) == 1:
            user = get_object_or_404(queryset, name=name)
        serializer = UserSerializer(user)
        # ssi es 404 ya responde. 
        # creamos carro si el cliente accede... 
        cd = ClientDetail.objects.get(client=user)
        sc = ShoppingCart.objects.filter(client_detail=cd).first()
        if(sc == None):
            print('saving')
            sc = ShoppingCart(client_detail=cd)
            sc.save()
        else:
            pass

        print()
        return Response(serializer.data)
        


class ClientDetailViewSet(viewsets.ModelViewSet):
    def retrieve(self, request, pk=None):
        queryset = ClientDetail.objects.all()
        serializer_class =ClientDetailSerializer

        

class ShoppingCartViewSet(viewsets.ModelViewSet): 

    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer
    # <Cart></Cart>
    def retrieve(self, request, pk=None):
        diccionario = request.query_params.dict()
        name = diccionario['user']
        #queryset = ShoppingCart.objects.all()
        #sc = get_object_or_404(queryset, pk=pk)
        #serializer = ShoppingCartSerializer(sc)
        user = User.objects.get(name=name)
        cd = ClientDetail.objects.get(client=user)
       
        sc = ShoppingCart.objects.get(client_detail=cd)
        cd = CartDetail.objects.filter(sc=sc)
        serializer_cart_d = CartDetailSerializer(cd, many=True)
        serializer_sc = ShoppingCartSerializer(sc)
        return Response([serializer_cart_d.data, serializer_sc.data])




# "agregar al carrito"
class CartDetailViewSet(viewsets.ModelViewSet):
    queryset = CartDetail.objects.all()
    serializer_class = CartDetailSerializer


    def retrieve(self, request, pk=None):
        diccionario = request.query_params.dict()
        user_name = diccionario['user']
        product_name = diccionario['product']
        product_cantidad = diccionario['product_cantidad']
        product_price = diccionario['product_price']
        user = User.objects.get(name=user_name)
        client_d = ClientDetail.objects.get(client=user)
        sc = ShoppingCart.objects.get(client_detail=client_d)
        sc_precio_previo = sc.sc_total_price
        sc.sc_total_price = sc_precio_previo + (int(product_price) * int(product_cantidad))
        sc.save()

        cd = CartDetail(sc=sc, product=product_name, product_quantity=product_cantidad)
        cart_d = CartDetail(sc=sc, product=product_name, product_quantity=product_cantidad)
        cart_d.save()
        return Response(product_name)

    def destroy(self, request, *args, **kwargs):
        diccionario = request.query_params.dict()
        product_name = diccionario['product']
        sc = diccionario['sc']
        sc_dict = json.loads(sc)
        sc_id = sc_dict['id']
        sc_total_price = sc_dict['sc_total_price']
        total = diccionario['total']
        sc = ShoppingCart.objects.get(id=sc_id)
        if sc.sc_total_price >0:
            sc.sc_total_price -= int(total)
            sc.save()

        
        # al sc_total_price del carro restarle total q seria de ese producto en especifico

        print(sc)
        print(total)
        cd = CartDetail.objects.get(product=product_name, sc=sc)
        self.perform_destroy(cd)
        cd = CartDetail.objects.filter(sc=sc)
        serializer_cart_d = CartDetailSerializer(cd, many=True)
        serializer_sc = ShoppingCartSerializer(sc)
        return Response([serializer_cart_d.data, serializer_sc.data])

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

    def list(self, request):
        diccionario = request.query_params.dict()
        print(diccionario)
        queryset = Sale.objects.all()
        serializer = SaleSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        print(request)
        diccionario = request.query_params.dict()
        keys = request.query_keys
        print(keys)
        name = diccionario['user']
        queryset = User.objects.all()
        user = get_object_or_404(queryset, name=name)
        client_d = ClientDetail.objects.get(client=user)
        sc = ShoppingCart.objects.filter(client_detail=client_d).first()
        

        if sc != None:
            sale = Sale(client_detail=client_d)
            sale.save()
            cd = CartDetail.objects.filter(sc=sc)
            for i in cd:
                product = i.product
                product_quantity = int(i.product_quantity)
                sale_d = SaleDetail(sale=sale, product=product, product_quantity=product_quantity)
                sale_d.save()
                serializer = SaleSerializer(sale)


            ShoppingCart.objects.filter(client_detail=client_d).delete()
            return Response(serializer.data)

        return Response('nada')

class SaleDetailViewSet(viewsets.ModelViewSet):
    queryset = SaleDetail.objects.all()
    serializer_class = SaleDetailSerializer

    def retrieve(self, request, pk=None):
        diccionario = request.query_params.dict()
        name = diccionario['user']
        queryset = User.objects.all()
        user = get_object_or_404(queryset, name=name)
        client_d = ClientDetail.objects.get(client=user)
        sale = Sale.objects.filter(client_detail=client_d)
        data = []
        for i in sale:
            # i : sale object
            sale_details = SaleDetail.objects.filter(sale=i)
            serializer = SaleDetailSerializer(sale_details, many=True)
            data.append(serializer.data)

        print(data)
        return Response(data)

from django.shortcuts import render
from django.http import JsonResponse
from .models import Product
import json
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer
from rest_framework import generics,status,mixins


class ProductRetriveViews(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


class ProductCreatViews(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductListViews(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class ProductDeleteViews(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    

class ProductUpdateViews(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

# @api_view(["GET","POST"])
# def product_view(request):
#     if request.method == "POST":
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
#     product = Product.objects.all()
#     data = {}
#     if product:
#         data = ProductSerializer(product,many = True)
#         print(data)
#     return Response(data.data)


class ProductViewsMixing(
    generics.GenericAPIView,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_create(self, serializer):
        name = serializer.validated_data.get("name")
        if name is None:
            name = "Je suis nulle"
        serializer.save(name=name)

    def perform_update(self, serializer):
        serializer.save()

    def get(self,request,*args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request,*args, **kwargs)
        return self.list(request,*args, **kwargs)
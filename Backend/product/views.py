from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.conf.urls import handler404
from .forms import ProductForm,ProductModelForm
from .models import Product
from .serializers import ProductSerializer
from rest_framework import authentication,generics,status,mixins,permissions
from .permissions import IsPerission

from django.views.decorators.csrf import csrf_exempt
def product_view(request,*args, **kwargs):
    if request.method == "POST":
        form = ProductModelForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            
    else:
        form = ProductModelForm()
    return render(request,'index.html',{'form':form})

class ProductRetriveViews(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    


class ListProductViewsMixing(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication,authentication.TokenAuthentication]
    permission_classes = [IsPerission]


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



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
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.SessionAuthentication]

    def perform_create(self, serializer):
        name = serializer.validated_data.get("name")
        if name is None:
            name = "Je suis nulle"
        serializer.save(name=name)

    def perform_update(self, serializer):
        serializer.save()

    def get(self,request,*args, **kwargs):
        pk = kwargs.get('pk')
        print(pk,kwargs)
        if pk is not None:
            return self.retrieve(request,*args, **kwargs)
        return self.list(request,*args, **kwargs)
    

def error_404(request,exception):
    return render(request,'pagenotfound.html')


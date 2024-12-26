from .models import Product
from .serializers import ProductSerializer
from rest_framework import authentication,generics,status,mixins,permissions
from .permissions import IsPerission

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
        if pk is not None:
            return self.retrieve(request,*args, **kwargs)
        return self.list(request,*args, **kwargs)
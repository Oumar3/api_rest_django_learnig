from django.urls import path,register_converter
from django.conf.urls import handler404
from .views import ProductViewsMixing,ListProductViewsMixing, product_view,ProductRetriveViews,error_404

handler404 =  'product.views.error_404'
handler404 =  'api.views.error_404'


urlpatterns = [
    path('<int:pk>/detail/',ProductViewsMixing.as_view(),name="product-detail"),
    path('create-product/',ListProductViewsMixing.as_view(),name="product-create"),
    path('<int:pk>/delete/',ProductViewsMixing.as_view(),name="product-delete"),
    path('<int:pk>/update/',ProductViewsMixing.as_view(),name="product-update"),
    path('',product_view,name="product-update"),

]

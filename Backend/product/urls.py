from django.urls import path
from .views import ProductViewsMixing, ProductRetriveViews,ProductCreatViews,ProductListViews,ProductDeleteViews,ProductUpdateViews

urlpatterns = [
    path('<int:pk>/detail/',ProductViewsMixing.as_view(),name="product-detail"),
    path('create-product/',ProductViewsMixing.as_view(),name="product-create"),
    path('product-list/',ProductViewsMixing.as_view(),name="product-list"),
    path('<int:pk>/delete/',ProductViewsMixing.as_view(),name="product-delete"),
    path('<int:pk>/update/',ProductViewsMixing.as_view(),name="product-update"),
]

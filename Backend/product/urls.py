from django.urls import path
from .views import ProductRetriveViews,ProductCreatViews,ProductListViews,ProductDeleteViews,ProductUpdateViews

urlpatterns = [
    path('<int:pk>/detail/',ProductRetriveViews.as_view(),name="product-detail"),
    path('create-product/',ProductCreatViews.as_view(),name="product-create"),
    path('product-list/',ProductListViews.as_view(),name="product-list"),
    path('<int:pk>/delete/',ProductDeleteViews.as_view(),name="product-delete"),
    path('<int:pk>/update/',ProductUpdateViews.as_view(),name="product-update"),
]

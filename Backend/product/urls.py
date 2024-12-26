from django.urls import path
from .views import ProductViewsMixing,ListProductViewsMixing
urlpatterns = [
    path('<int:pk>/detail/',ProductViewsMixing.as_view(),name="product-detail"),
    path('create-product/',ListProductViewsMixing.as_view(),name="product-create"),
    path('<int:pk>/delete/',ProductViewsMixing.as_view(),name="product-delete"),
    path('<int:pk>/update/',ProductViewsMixing.as_view(),name="product-update"),
]

from django.urls import path
# from . import views
# from product.views import product_view

# urlpatterns = [
#     path('',views.api_views,name="api_views"),
#     path('product',product_view,name="product_views")
# ]

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('auth/',obtain_auth_token),
]


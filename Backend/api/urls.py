from django.urls import path
from . import views


urlpatterns = [
    path('',views.api_views,name="api_views")
]

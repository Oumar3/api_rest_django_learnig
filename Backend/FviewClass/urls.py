from django.urls import path
from .views import ArticleViews

urlpatterns = [
    path('',ArticleViews.as_view(),name="article-list"),
    # path('<int:pk>/detail/',ArticleViews.as_view(),name="detail-article"),
]
from django.urls import path
from app1.api.views import ArticleCreateAPIView,ArticleDetailAPIView,JournalistListCreateAPIView

urlpatterns = [
    path("articles/", ArticleCreateAPIView.as_view(), name="article-list"),
    path("articles/<int:pk>/", ArticleDetailAPIView.as_view(), name="article-detail"),
    path("journalists/", JournalistListCreateAPIView.as_view(), name="journalists-list ")



]

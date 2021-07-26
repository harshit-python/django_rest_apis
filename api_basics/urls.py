from django.urls import path
from .views import ArticleAPIView, ArticleDetails

urlpatterns = [
    path('articles/', ArticleAPIView.as_view()),
    path('article_detail/<int:pk>/', ArticleDetails.as_view()),
]
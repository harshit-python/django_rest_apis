from django.urls import path
from .views import GenericAPIView

urlpatterns = [
    path('articles/', GenericAPIView.as_view()),
    path('articles/<int:pk>/', GenericAPIView.as_view()),
]
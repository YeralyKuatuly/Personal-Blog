from django.urls import path
from .views import (HomePageView, ArticleDetailView, DashboardView, ArticleCreateView, ArticleUpdateView,
                    ArticleDeleteView)

app_name = 'blog'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('article/add/', ArticleCreateView.as_view(), name='article_create'),
    path('article/edit/<int:pk>/', ArticleUpdateView.as_view(), name='article_update'),
    path('article/delete/<int:pk>/', ArticleDeleteView.as_view(), name='article_delete'),
]

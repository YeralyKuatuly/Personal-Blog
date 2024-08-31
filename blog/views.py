from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Article
from .forms import ArticleForm


# Guest Section
class HomePageView(ListView):
    model = Article
    template_name = 'blog/home.html'
    context_object_name = 'articles'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'
    context_object_name = 'article'


# Admin Section
class DashboardView(ListView):
    model = Article
    template_name = 'blog/dashboard.html'
    context_object_name = 'articles'


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/article_form.html'
    success_url = reverse_lazy('blog:dashboard')


class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/article_form.html'
    success_url = reverse_lazy('blog:dashboard')


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'blog/article_confirm_delete.html'
    success_url = reverse_lazy('blog:dashboard')

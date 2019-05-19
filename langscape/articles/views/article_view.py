# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView, DetailView

from ..models import Article, Comment


class ArticleListView(ListView):
    model = Article

    def get_queryset(self):
        queryset = super(ArticleListView, self).get_queryset()

        q = self.request.GET.get("q")
        if q:
            return queryset.filter(title__icontains=q)
        return queryset


class ArticleDetailView(DetailView):
    model = Article

    def get_context_data(self, **kwargs):
        article = self.object
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(article=article)
        return context

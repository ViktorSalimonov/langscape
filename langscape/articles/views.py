# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView

from .models import Article
from .utils import check_member_rights


class ArticleListView(ListView):
    model = Article


class ArticleDetailView(DetailView):
    model = Article


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['title', 'difficulty', 'text']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('articles:detail', kwargs={'pk': self.object.pk})

    def dispatch(self, request, *args, **kwargs):
        request = check_member_rights(request)
        return super(ArticleUpdateView, self).dispatch(
                                                    request, *args, **kwargs)

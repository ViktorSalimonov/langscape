# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from .models import Article
from .utils import check_member_rights


class ArticleListView(ListView):
    model = Article


class ArticleDetailView(DetailView):
    model = Article


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    fields = ['title', 'difficulty', 'text']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('articles:detail', kwargs={'pk': self.object.pk})


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('articles:list')

    def dispatch(self, request, *args, **kwargs):
        request = check_member_rights(request)
        return super(ArticleDeleteView, self).dispatch(
                                                    request, *args, **kwargs)

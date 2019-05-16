# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView

from .models import Article
from .utils import check_member_rights


class ArticleActionMixin(object):
    fields = ['title', 'difficulty', 'text']

    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.info(self.request, self.success_msg)
        return super(ArticleActionMixin, self).form_valid(form)


class ArticleListView(ListView):
    model = Article


class ArticleDetailView(DetailView):
    model = Article


class ArticleCreateView(LoginRequiredMixin, ArticleActionMixin, CreateView):
    model = Article
    success_msg = "Aricle is created!"
    success_url = reverse_lazy('articles:list')


class ArticleUpdateView(LoginRequiredMixin, ArticleActionMixin, UpdateView):
    model = Article
    success_msg = "Aricle is updated!"
    success_url = reverse_lazy('articles:list')


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('articles:list')

    def dispatch(self, request, *args, **kwargs):
        request = check_member_rights(request)
        return super(ArticleDeleteView, self).dispatch(
                                                    request, *args, **kwargs)

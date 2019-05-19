# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView

from .forms import CommentForm
from .models import Article, Comment
# from .utils import check_member_rights


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


class CommentActionMixin(object):

    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.info(self.request, self.success_msg)
        return super(CommentActionMixin, self).form_valid(form)


class CommentCreateView(LoginRequiredMixin, CommentActionMixin, CreateView):
    model = Comment
    form_class = CommentForm
    success_msg = "Comment is created!"
    success_url = reverse_lazy('articles:list')

    def form_valid(self, form):
        form.instance.article = get_object_or_404(Article,
                                                  pk=self.kwargs['pk'])
        return super(CommentCreateView, self).form_valid(form)


# class CommentUpdateView(LoginRequiredMixin, CommentActionMixin, UpdateView):
#     model = Comment
#     form_class = CommentForm
#     success_msg = "Article is updated!"
#     success_url = reverse_lazy('articles:list')


# class CommentDeleteView(DeleteView, CommentActionMixin, UpdateView):
#     model = Article
#     success_msg = "Comment is deleted!"
#     success_url = reverse_lazy('articles:list')

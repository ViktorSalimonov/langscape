# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView

from ..forms import CommentForm
from ..models import Article, Comment, Member


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

    def get_success_url(self, **kwargs):
        return reverse_lazy('articles:detail',
                            kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        form.instance.article = get_object_or_404(Article,
                                                  pk=self.kwargs['pk'])
        form.instance.author = get_object_or_404(Member,
                                                 pk=self.request.user.id)
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

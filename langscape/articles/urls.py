from django.conf.urls import url

from langscape.articles.views import ArticleListView, ArticleDetailView

urlpatterns = [
    url(r'^$', ArticleListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', ArticleDetailView.as_view(), name='details'),
]

from django.conf.urls import url

from . import views

urlpatterns = [
    url(regex=r'^$',
        view=views.ArticleListView.as_view(),
        name="list"),
    url(regex=r'^(?P<pk>\d+)$',
        view=views.ArticleDetailView.as_view(),
        name='detail'),
    url(regex=r'^(?P<pk>\d+)/update/$',
        view=views.ArticleUpdateView.as_view(),
        name='update'),
    url(regex=r'^(?P<pk>\d+)/delete/$',
        view=views.ArticleDeleteView.as_view(),
        name='delete'),
]

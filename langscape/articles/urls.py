from django.conf.urls import include, url
from rest_framework import routers

from .api.views import ArticleListAPIView
from views import article_view, comment_view

router = routers.DefaultRouter()
router.register(r'articles', ArticleListAPIView)


urlpatterns = [
    # url(regex=r'',
    #     view=views.ArticleDashboardView.as_view(),
    #     name='dashboard'),
    url(r'^$',
        article_view.ArticleListView.as_view(),
        name="list"),
    url(r'^(?P<pk>\d+)/$',
        article_view.ArticleDetailView.as_view(),
        name='detail'),
    url(r'^(?P<pk>\d+)/comment/$',
        comment_view.CommentCreateView.as_view(),
        name='add_comment'),
    url(r'^(?P<pk>\d+)/comment/delete$',
        comment_view.CommentDeleteView.as_view(),
        name='delete_comment'),
    url('api/',
        include(router.urls)),
]

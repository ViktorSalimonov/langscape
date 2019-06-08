from django.conf.urls import url

from views import article_view, comment_view


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
]

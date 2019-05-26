from django.conf.urls import url

from views import article_view, comment_view

urlpatterns = [
    # url(regex=r'',
    #     view=views.ArticleDashboardView.as_view(),
    #     name='dashboard'),
    url(regex=r'^$',
        view=article_view.ArticleListView.as_view(),
        name="list"),
    url(regex=r'^(?P<pk>\d+)/$',
        view=article_view.ArticleDetailView.as_view(),
        name='detail'),
    url(regex=r'^(?P<pk>\d+)/comment/$',
        view=comment_view.CommentCreateView.as_view(),
        name='add_comment'),
    url(regex=r'^(?P<pk>\d+)/comment/delete$',
        view=comment_view.CommentDeleteView.as_view(),
        name='delete_comment'),
]

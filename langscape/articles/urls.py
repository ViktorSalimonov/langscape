from django.conf.urls import url

from . import views

urlpatterns = [
    # url(regex=r'',
    #     view=views.ArticleDashboardView.as_view(),
    #     name='dashboard'),
    url(regex=r'^$',
        view=views.ArticleListView.as_view(),
        name="list"),
    url(regex=r'^(?P<pk>\d+)/$',
        view=views.ArticleDetailView.as_view(),
        name='detail'),
    url(regex=r'^(?P<pk>\d+)/comment/$',
        view=views.CommentCreateView.as_view(),
        name='add_comment'),
]

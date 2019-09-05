from django.views.generic.list import ListView

from langscape.articles.models import Article


class ArticleListView(ListView):
    """Common list view for articles."""

    model = Article
    template_name = "article_list.html"
    context_object_name = "articles"
    paginate_by = 10

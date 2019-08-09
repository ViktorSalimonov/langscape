from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from langscape.articles.models import Article
from langscape.api.serializers import ArticleSerializer


class ArticleListAPIView(viewsets.ModelViewSet):

    queryset = Article.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ArticleSerializer
    lookup_field = 'uuid'

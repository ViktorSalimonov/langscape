from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..articles.models import Article
from .serializers import ArticleSerializer


class ArticleListAPIView(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = ArticleSerializer
    lookup_field = 'uuid'

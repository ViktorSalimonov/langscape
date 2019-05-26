from rest_framework import serializers

from ..articles.models import Article


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = (
            'uuid',
            'title',
            'created',
            'difficulty',
            'author',
            'content'
        )

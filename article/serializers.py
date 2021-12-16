from rest_framework.serializers import ModelSerializer

from article.models import Article, Board


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class BoardSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'

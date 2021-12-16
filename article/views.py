# Create your views here.
from django.http import HttpRequest
from django.shortcuts import redirect
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from article.models import Article, Board
from article.serializers import ArticleSerializer, BoardSerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    @action(detail=True, methods=['get'])
    def board(self, request: HttpRequest, pk):
        pk = int(pk)
        board: Board = Board.objects.get(id=pk)
        return Response(BoardSerializer(board).data)


class BoardViewSet(ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    @action(detail=True, methods=['get'])
    def articles(self, request: HttpRequest, pk=None):
        board: Board = self.get_object()
        article_list: list[Article] = board.article_set.order_by('-id')
        article_serializer = ArticleSerializer(article_list, many=True)

        return Response(article_serializer.data)

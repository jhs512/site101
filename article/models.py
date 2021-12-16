from django.db import models


class Board(models.Model):
    reg_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.id}, {self.name}'


# Create your models here.
class Article(models.Model):
    reg_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()

    @property
    def recent_users(self):
        return self.board.name

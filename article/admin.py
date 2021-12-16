from django.contrib import admin

# Register your models here.
from article.models import Article


class ArticleAdmin(admin.ModelAdmin):
    class Meta:
        model = Article


admin.site.register(Article, ArticleAdmin)

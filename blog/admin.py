from django.contrib import admin
from .models import Article


@admin.register(Article)    # admin.site.register(ArticleAdmin, Article)
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title', 'author', 'publish', 'status')
    list_filter = ('status', 'publish')
    list_editable = ('status',)
    search_fields = ('title', 'content')
    raw_id_fields = ('author',)

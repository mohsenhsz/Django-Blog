from django.shortcuts import render, get_object_or_404
from .models import Article
# from django.views import View

def Index(request):
    articles = Article.publish_objects.all()
    return render(request, 'blog/index.html', {'articles':articles})


def PostsDetail(request, pk, myslug):
    article = get_object_or_404(Article, id=pk, slug=myslug)
    return render(request, 'blog/post_details.html', {"article":article})


""" DO with class base views """
# class Index(views.ListView):
#     # model=Article
#     context_object_name = 'posts'
#     template_name = 'blog/index.html'

#     def get_queryset(self):
#         return Article.objects.all().order_by('-publish')


# class PostsDetail(views.DetailView):
#     context_object_name = 'post'
#     template_name = 'blog/post_details.html'
#     slug_field = 'slug'
#     slug_url_kwarg = 'myslug'

#     def get_queryset(self, **kwargs):
#         return Article.objects.filter(id=self.kwargs['pk'] , slug=self.kwargs['myslug'])

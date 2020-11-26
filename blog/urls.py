from django.urls import path
from .views import Index, PostsDetail

urlpatterns = [
    path('', Index, name='index'),
    path('<int:pk>/<slug:myslug>', PostsDetail, name='post_detail'),
    
]

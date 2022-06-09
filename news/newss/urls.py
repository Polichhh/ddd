from django.contrib import admin
from django.urls import path, include
from .views import  (PostList, PostDetail, NewsSearch, NewsCreate, ArticleCreate, NewsEdit, ArticleEdit, NewsDelete, ArticleDelete)

# urlpatterns = [
#     path('default', default)
# ]

urlpatterns = [

    path('news/', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
    # path('create/', create_post.as_view(), name='post_create'),
    path('news/search/', NewsSearch.as_view(), name='news_search'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('articles/create/', ArticleCreate.as_view(), name='article_create'),
    path('news/<int:pk>/edit/', NewsEdit.as_view(), name='news_edit'),
    path('articles/<int:pk>/edit/', ArticleEdit.as_view(), name='article_edit'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('articles/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),


]


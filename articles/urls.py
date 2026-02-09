from django.urls import path
from .views import (
  ArticleCreatView,
  ArticleListView,
  ArticleDetailView,
  ArticleUpdateView,
  ArticleDeleteView,
  ArticleCommentCreateView,
  comments_list,
  )

urlpatterns = [
  path('', ArticleListView.as_view(), name='article_list'),
  path('new/',ArticleCreatView.as_view(), name='article_new'),
  path('articles/comment/new', ArticleCommentCreateView.as_view(), name='comment_new'),
  path('articles/<int:pk>/comments/', comments_list, name='comments_lists'),
  path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
  path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
  path('<int:pk>/delete', ArticleDeleteView.as_view(), name='article_delete'),
  
] 
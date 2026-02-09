from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, render
from django.core.exceptions import PermissionDenied

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Article, Comment

# Create your views here.
  

class ArticleListView(ListView):
  model = Article
  template_name = "article_list.html"


class ArticleDetailView(DetailView):
  model = Article
  template_name = 'article_detail.html'


class ArticleCreatView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
  model = Article
  fields = ('title','summary','body','photo',)
  template_name = 'article_new.html'

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)
  
  def test_func(self):
    return self.request.user.is_superuser 

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ('title', 'summary', 'body', 'photo')
    template_name = 'article_edit.html'

    def test_func(self):
      obj = self.get_object()
      return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
  model = Article
  template_name = 'article_delete.html'
  success_url = reverse_lazy('article_list')

  
  def test_func(self):
    obj = self.get_object()
    return obj.author == self.request.user
  

class ArticleCommentCreateView(CreateView):
  model = Comment
  fields = ('article','comment','author',)
  template_name = 'comment_new.html'


def comments_list(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'comments_lists.html', {
        'article': article
    })
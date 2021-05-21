from django.shortcuts import render

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from .models import Post, Comment


# Create your views here.
class BlogListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','author', 'body'] #
    template_name = 'post_new.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(
    LoginRequiredMixin, UserPassesTestMixin, UpdateView
    ):
    model = Post
    fields = ['title', 'body']
    template_name = 'post_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class BlogDeleteView(
    LoginRequiredMixin, UserPassesTestMixin, DeleteView
    ):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['comment', 'author']
    template_name = 'post_detail.html'
      
    def form_valid(self, form):
       form.instance.author = self.request.user
       form.instance.post = Post.objects.get(pk=self.kwargs['post_pk'])
       return super().form_valid(form)
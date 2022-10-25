from time import timezone
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.forms import PostForm, CommentForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from blog.models import Post, Comment
# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'
    
class PostListView(ListView):
    model = Post
    
    def get_queryset(self):
        return Post.obects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post
    
class CreatePostView(CreateView, LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'blog/post/detail.html'
    form_class = PostForm
    model = Post
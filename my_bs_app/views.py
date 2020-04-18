from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView

from .models import Post


class PostList(ListView):
    #queryset = Post.objects.filter(status=1).order_by('-created_on')
    queryset = Post.objects.all()
    context_object_name = 'Post list'
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'

class AboutView(TemplateView):
    template_name = "about.html"

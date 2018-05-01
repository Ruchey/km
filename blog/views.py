from django.shortcuts import render
from django.views import generic
from .models import Post

import pdb


class ListView(generic.ListView):
    model = Post
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts_list'
    # pdb.set_trace()

    def get_queryset(self):
        return Post.objects.order_by('-published_date')

class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post_detail'
    # pdb.set_trace()

    def get_queryset(self):
        return Post.objects
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = "home.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    # context_object_name = blog_detail


# with the above edits, we can use blog_detail as the context object name
# so that will override the context object name naturally provided by django for us
# which is #object or #post(lower case of the db table name)

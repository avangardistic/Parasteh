from django.views.generic import DetailView, ListView

from .models import Post


class PostList(ListView):
    model = Post
    context_object_name = "posts"
    queryset = Post.objects.all()
    template_name = "blog/post_list.html"


class PostDetail(DetailView):
    model = Post
    context_object_name = "post"

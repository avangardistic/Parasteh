from django.views.generic import DetailView, ListView

from .models import Post, Category


class PostList(ListView):
    model = Post
    context_object_name = "posts"
    queryset = Post.objects.all()
    template_name = "blog/post_list.html"


class PostDetail(DetailView):
    model = Post
    context_object_name = "post"


class PostFilter(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "blog/post_list.html"
 
    def get_queryset(self):
        category = Category.objects.get(slug=self.kwargs["category_pk"])
        return Post.objects.filter(category=category.pk)

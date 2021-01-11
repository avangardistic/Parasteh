from django.db import models

STATUS = ((0, "Draft"), (1, "Publish"))


class PostManager(models.Manager):
    def change_status(self, pk, new_status):
        post = Post.objects.get(pk=pk)
        post.status = new_status
        post.save()


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    author = models.ForeignKey(
        "consumers.Consumer", on_delete=models.CASCADE, related_name="blog_author"
    )
    category = models.ForeignKey(
        "blog.Category", on_delete=models.CASCADE, related_name="blog_category"
    )

    subtitle = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="posts/", blank=True, null=True)
    content = models.TextField()

    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    objects = PostManager()

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title

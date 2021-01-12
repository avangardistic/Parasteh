from django.test import TestCase

from blog.models import Category, Post
from consumers.models import Consumer


class PostTests(TestCase):
    def setUp(self):
        self.author = Consumer.objects.create_user(
            email="test@example.com", password="fooBar123"
        )
        self.category = Category(title="Test Category", slug="test-category")
        self.post = Post(
            title="This is a test",
            slug="this-is-a-test",
            author=self.author,
            category=self.category,
            content="this is a test content",
            status=0,
        )
        self.author.save()
        self.category.save()
        self.post.save()

    def test_post_creation(self):
        self.assertEqual(len(Category.objects.all()), 1)
        self.assertEqual(len(Post.objects.all()), 1)

        self.assertEqual(self.post.status, 0)

    def test_post_changing_status(self):
        Post.objects.change_status(self.post.pk, 1)
        post = Post.objects.get(pk=1)
        self.assertEqual(post.status, 1)

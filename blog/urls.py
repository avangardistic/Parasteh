from django.urls import path

from .views import PostDetail, PostList

urlpatterns = [path("", PostList.as_view()), path("<slug:slug>/", PostDetail.as_view())]

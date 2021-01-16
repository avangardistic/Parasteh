from django.urls import path

from .views import PostDetail, PostList, PostFilter

urlpatterns = [
    path("", PostList.as_view()), 
    path("<slug:slug>/", PostDetail.as_view()),
    path("category/<slug:category_pk>", PostFilter.as_view()),
] 

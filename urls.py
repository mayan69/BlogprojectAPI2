from django.urls import path
from .views import BlogPostByCategoryListView,BlogPostDeleteView,BlogPostUpdateView,BlogPostByUserListView,CategoryCreateAPIView,CategoryListAPIView,BlogPostListAPIView,BlogPostByCategoryListView,BlogPostCreateView,BlogPostDetailView
# from .views import Category Create__ListEndPoint,BlogPostList_CreateEndpoint,BlogPostByUserListView,BlogPostDetailEndPoint,BlogPostByCategoryListView

urlpatterns=[
    path('users/create-post/',BlogPostCreateView.as_view(), name='blogpost-create'),
    path('users/update/<int:pk>/',BlogPostUpdateView.as_view(), name='blogpost-update'),
    path('users/delete/<int:pk>/', BlogPostDeleteView.as_view(), name='blogpost-delete'),
    path('categories/create/',CategoryCreateAPIView.as_view(), name='category-create'),
    path('categories/posts/<int:pk>/',BlogPostByCategoryListView.as_view(),name='posts-by-category'),
    path('posts/detail/<int:pk>/', BlogPostDetailView.as_view(), name='post-detail'),
    path('user/posts/<int:pk>/', BlogPostByUserListView.as_view(), name='posts-by-user'),
    path('posts/',BlogPostListAPIView.as_view(), name='blogpost-list'),
    path('categories/list/',CategoryListAPIView.as_view(), name='categories-list')
]
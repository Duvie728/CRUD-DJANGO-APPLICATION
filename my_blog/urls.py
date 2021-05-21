from django.urls import path
from . import views
from .views import (
    BlogListView, 
    BlogDetailView, 
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    CommentCreateView,
)

#app_name = 'posts'
urlpatterns = [
    path('post/<int:post_pk>/comment/', 
        CommentCreateView.as_view(), name='add_comment'),
    path('post/<int:pk>/delete/',BlogDeleteView.as_view(), name='post_delete'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/',
        BlogUpdateView.as_view(), name='post_edit'),
    path('', BlogListView.as_view(), name='home'),
    #path('post/', BlogListView.as_view(template_name='home.html'), name="home"),
    
]
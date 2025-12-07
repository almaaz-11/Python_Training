# blog/urls.py
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'blog'

urlpatterns = [
    # Posts
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('create/', views.PostCreateView.as_view(), name='create_post'),
    path('post/<slug:slug>/edit/', views.PostUpdateView.as_view(), name='edit_post'),
    path('post/<slug:slug>/delete/', views.PostDeleteView.as_view(), name='delete_post'),
    
    # User posts
    path('my-posts/', views.UserPostListView.as_view(), name='my_posts'),
    
    # Authentication
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
]


# blog/views.py
from django.shortcuts import redirect
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Post, Comment
from .forms import PostForm, CommentForm, SignUpForm

class PostListView(ListView):
    """List all published posts with search and filtering."""
    
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10
    
    def get_queryset(self):
        """Filter posts and add search."""
        queryset = Post.objects.filter(
            is_published=True
        ).select_related('author')
        # What: select_related fetches author data in one query
        # Why: Avoids N+1 query problem (one query per post)
        
        # Add search functionality
        search = self.request.GET.get('q')
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) |  # Case-insensitive search
                Q(content__icontains=search)
            )
        
        return queryset.order_by('-created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        return context

class PostDetailView(DetailView):
    """Display single post with comments."""
    
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    
    def get_queryset(self):
        """Only show published posts."""
        return Post.objects.filter(is_published=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        post = self.get_object()
        
        # Increment view count
        post.views += 1
        post.save(update_fields=['views'])
        
        # Add comments
        context['comments'] = post.comments.filter(is_approved=True)
        
        if self.request.user.is_authenticated:
            context['comment_form'] = CommentForm()
        
        return context
    
    def post(self, request, *args, **kwargs):
        """Handle comment submission."""
        self.object = self.get_object()
        
        if not request.user.is_authenticated:
            messages.error(request, 'You must be logged in to comment.')
            return redirect('login')
        
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.author = request.user
            comment.save()
            messages.success(request, 'Comment added! Awaiting approval.')
            return redirect('blog:post_detail', slug=self.object.slug)
        
        context = self.get_context_data(object=self.object)
        context['comment_form'] = form
        return self.render_to_response(context)

class PostCreateView(LoginRequiredMixin, CreateView):
    """Create a new post (login required)."""
    
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    login_url = 'login'
    
    def form_valid(self, form):
        """Set author and is_published."""
        form.instance.author = self.request.user
        form.instance.is_published = True
        messages.success(self.request, 'Post created successfully!')
        return super().form_valid(form)

class PostUpdateView(UserPassesTestMixin, UpdateView):
    """Edit a post (only author or admin)."""
    
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    
    def test_func(self):
        """Check if user is author or admin."""
        post = self.get_object()
        return (
            self.request.user == post.author or
            self.request.user.is_superuser
        )
    
    def handle_no_permission(self):
        messages.error(self.request, 'You cannot edit this post.')
        return redirect('blog:post_detail', slug=self.get_object().slug)

class PostDeleteView(UserPassesTestMixin, DeleteView):
    """Delete a post (only author or admin)."""
    
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    
    def test_func(self):
        post = self.get_object()
        return (
            self.request.user == post.author or
            self.request.user.is_superuser
        )

class UserPostListView(ListView):
    """List posts by a specific user."""
    
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 10
    
    def get_queryset(self):
        """Get posts by user."""
        author = self.request.user
        return Post.objects.filter(author=author).order_by('-created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_user'] = self.request.user
        return context

# Authentication views
class SignUpView(CreateView):
    """User registration."""
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        messages.success(self.request, 'Account created! Please log in.')
        return super().form_valid(form)

class CustomLoginView(LoginView):
    """User login."""
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

class CustomLogoutView(LogoutView):
    """User logout."""
    next_page = 'blog:post_list'

class UserProfileView(LoginRequiredMixin, DetailView):
    """User profile page."""
    model = User
    template_name = 'blog/profile.html'
    context_object_name = 'profile_user'
    login_url = 'login'
    
    def get_object(self):
        """Always get current user's profile."""
        return self.request.user
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(author=user)
        context['total_views'] = sum(p.views for p in context['posts'])
        return context

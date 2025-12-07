from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from .models import Post, Comment
from .forms import PostForm, CommentForm

def post_list(request):
    """Display list of all published posts."""
    # Get all published posts, ordered by newest first
    posts = Post.objects.filter(is_published=True).order_by('-created_at')
    
    context = {
        'posts': posts,
        'title': 'Blog Posts'
    }
    return render(request, 'myapp/post_list.html', context)

def post_detail(request, slug):
    """Display single post with comments and comment form."""
    # Get the post by slug (URL-friendly identifier)
    post = get_object_or_404(Post, slug=slug, is_published=True)
    
    # Increment view count
    post.views += 1
    post.save(update_fields=['views'])
    # What: update_fields only updates specified fields (more efficient)
    # Why: Saves database query time vs updating all fields
    
    # Get approved comments only
    comments = post.comments.filter(is_approved=True)
    
    if request.method == 'POST':
        # User submitted a comment
        form = CommentForm(request.POST)
        if form.is_valid():
            # Create comment but don't save yet
            comment = form.save(commit=False)
            comment.post = post  # Link comment to this post
            comment.save()
            messages.success(request, 'Comment added! Awaiting approval.')
            return redirect('post_detail', slug=post.slug)
    else:
        # GET request - show empty comment form
        form = CommentForm()
    
    context = {
        'post': post,
        'comments': comments,
        'form': form,
        'title': post.title
    }
    return render(request, 'myapp/post_detail.html', context)

def create_post(request):
    """Create a new blog post."""
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.username
            post.is_published = False  # Draft by default
            post.save()
            messages.success(request, 'Post created! Submit for review.')
            return redirect('edit_post', slug=post.slug)
    else:
        form = PostForm()
    
    context = {'form': form, 'title': 'Create Post'}
    return render(request, 'myapp/post_form.html', context)

def edit_post(request, slug):
    """Edit an existing blog post."""
    post = get_object_or_404(Post, slug=slug)
    
    # Check permission (only author or admin can edit)
    if request.user.username != post.author and not request.user.is_superuser:
        messages.error(request, 'You cannot edit this post.')
        return redirect('post_detail', slug=post.slug)
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'Post updated!')
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    
    context = {'form': form, 'title': 'Edit Post', 'post': post}
    return render(request, 'myapp/post_form.html', context)

def delete_post(request, slug):
    """Delete a blog post."""
    post = get_object_or_404(Post, slug=slug)
    
    # Check permission
    if request.user.username != post.author and not request.user.is_superuser:
        messages.error(request, 'You cannot delete this post.')
        return redirect('post_detail', slug=post.slug)
    
    if request.method == 'POST':
        # Confirm deletion
        post.delete()
        messages.success(request, 'Post deleted!')
        return redirect('post_list')
    
    context = {'post': post}
    return render(request, 'myapp/post_confirm_delete.html', context)



# from turtle import title
# from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse, JsonResponse
# from django.views import View
# from django.views.generic import ListView, DetailView, CreateView
# from .models import Post, Comment
# from django.urls import reverse_lazy
# from .forms import PostForm, CommentForm

# # Create your views here.
# # def post_list(request):
# #     posts = Post.objects.filter(is_published=True).order_by('-created_at')
# #     return render(request, 'myapp/post_list.html', {'posts': posts})

# # def post_detail(request, post_id):
# #     post = get_object_or_404(Post, id=post_id, is_published=True)
# #     comments = post.comments.all()

# #     context = {
# #         'post': post,
# #         'comments': comments,
# #     }

# #     return render(request, 'myapp/post_detail.html', context)

# class PostListView(ListView):
#     model = Post
#     template_name = 'myapp/post_list.html'
#     context_object_name = 'posts'
#     paginate_by = 10

#     def get_queryset(self):
#         return Post.objects.filter(is_published=True).order_by('-created_at')

# class PostDetailView(DetailView):
#     model = Post
#     template_name = 'myapp/post_detail.html'
#     context_object_name = 'post'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['comments'] = self.object.comments.all()
#         return context

# def api_posts(request):
#     posts = Post.objects.filter(is_published=True).values()
#     return JsonResponse(list(posts), safe=False)

# def create_post(request):
#     if request.method == "POST":

#         form = PostForm(request.POST)

#         if form.is_valid():

#             post = form.save(commit=False)

#             post.author = request.user.username

#             post.save()

#             messages.success(request, "Post created successfully")

#             return redirect('myapp:post_detail', pk=post.pk)

#         else:

#             form = PostForm()

#         context = {
#             'form': form,
#             'mode': 'create',
#             'title': 'Create New Post',
#         }

#         return render(request, 'myapp/post_form.html', context)

# def edit_post(request, pk):

#     post = get_object_or_404(Post, pk=pk)

#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)

#         if form.is_valid():

#             post = form.save()
#             messages.success(request, "Post updated successfully")
#             return redirect('myapp:post_detail', pk=post.pk)
#         else:
#             form = PostForm(instance=post)
#         context = {
#             'form': form,
#             'mode': 'edit',
#             'title': 'Edit Post',
#         }
#         return render(request, 'myapp/post_form.html', context)


from dataclasses import fields
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views import View
# from django.http import HttpResponse

# Create your views here.
# class HomeView(View):
#     def get(self, request):
#         return HttpResponse("Hello World")

# class AboutView(View):
#     def get(self, request):
#         return HttpResponse("This is about page")

class HomeView(TemplateView):
    template_name = 'learncbv/home.html'

class ProfileView(TemplateView):
    template_name = 'learncbv/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["username"] = 'Almaaz'
        context['skills'] = ['python', 'jave', 'php']
        return context

class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'posts/post_form.html'
    success_url = reverse_lazy('post_list')

    login_url = 'login'
    redirect_field_name = 'next'

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'posts/post_form.html'
    success_url = reverse_lazy('post_list')

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')


    



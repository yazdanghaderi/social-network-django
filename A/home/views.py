from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import Post
from django.contrib import messages

class HomeView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, "home/index.html", context={"posts":posts})

class PostDetailView(View):
    def get(self, request, post_id, post_slug):
        post = Post.objects.get(id=post_id, slug=post_slug)
        return  render(request, "home/detail.html", {"post":post})



class PostDeleteView(LoginRequiredMixin, View):
    login_url = 'account:user_login'
    def get(self, request, post_id):
        post = Post.objects.get(pk=post_id)
        if post.user.id == request.user.id:
            post.delete()
            messages.success(request, "post is deleted successfully.", 'success')
        else:
            messages.error(request, "you cant deleted this post.", 'danger')
        return redirect("home:home")
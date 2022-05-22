from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import Post
from django.contrib import messages
from .forms import PostCreateAndUpdateForm
from django.utils.text import slugify

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

class PostUpdateView(LoginRequiredMixin, View):
    login_url = 'account:user_login'
    form_class = PostCreateAndUpdateForm

    def setup(self, request, *args, **kwargs):
        self.post_instance = Post.objects.get(id=kwargs["post_id"])
        return super().setup(request, *args, **kwargs)


    def dispatch(self, request, *args, **kwargs):
        post = self.post_instance
        if not request.user.id == post.user.id:
            messages.error(request, "user not correct.", "danger")
            return redirect("home:home")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        post = self.post_instance
        form = self.form_class(instance=post)
        return render(request, "home/update.html", context={"form":form})

    def post(self, request, *args, **kwargs):
        post = self.post_instance
        form = self.form_class(request.POST, instance=post)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.slug = slugify(form.cleaned_data['body'][:30])
            new_post.save()
            messages.success(request, "you updated this post", 'success')
            return redirect("home:post_detail", post.id,post.slug)

class PostCreateView(LoginRequiredMixin, View):
    login_url = 'account:user_login'
    form_class = PostCreateAndUpdateForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, "home/create.html", context={"form":form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.slug = slugify(form.cleaned_data['body'][:30])
            new_post.user = request.user
            new_post.save()
            messages.success(request, "you create this post", 'success')
            return redirect("home:post_detail", new_post.id, new_post.slug)
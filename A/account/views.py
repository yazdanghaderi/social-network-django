from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from .forms import UserRegisterationForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from home.models import Post
# Create your views here.


class UserRegisteraion(View):
    form_class = UserRegisterationForm
    template_name = "account/register.html"
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home:home")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, context={"form":form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            User.objects.create_user(username=cd["username"],email=cd["email"],password=cd["password1"])
            messages.success(request, "successfully", "success")
            return redirect("home:home")
        else:
            return render(request, self.template_name, context={"form": form})


class UserLogin(View):
    form_class = UserLoginForm
    template_name ="account/login.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home:home")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, context={"form":form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd["username"], password=cd["password"])
            if user is not None:
                login(request, user)
                ms = cd["username"] + " is login"
                messages.success(request, ms , "success")
                return redirect("home:home")
            messages.success(request, "user info is not correct", "warning")
        return render(request, self.template_name, context={"form":form})


class UserLogout(LoginRequiredMixin, View):
    login_url = 'account:user_login'
    def get(self, request):
        logout(request)
        messages.success(request, "user logout successfully.", "success")
        return redirect("home:home")


class UserProfileView(LoginRequiredMixin, View):
    login_url = 'account:user_login'
    def get(self, request, pid):
        user = User.objects.get(id=pid)
        posts = Post.objects.filter(user=user)
        return render(request, "account/profile.html", context={"user":user, "posts":posts})

class UserPasswordResetView(auth_views.PasswordResetView):
    template_name = "account/password_reset_form.html"
    success_url = reverse_lazy("account:password_reset_done")
    email_template_name = "account/password_reset_email.html"

class UserPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = "account/password_reset_done_view.html"


class UserPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = "account/password_reset_confirm.html"
    success_url = reverse_lazy("account:password_reset_complete")

class UserPassowrdResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = "account/password_reset_complete.html"
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterationForm
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.


class RegisterUser(View):
    form_class = UserRegisterationForm
    template_name = "account/register.html"
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



from django.shortcuts import render
from django.views import View
from .forms import UserRegisterationForm
# Create your views here.


class RegisterUser(View):
    def get(self, request):
        form = UserRegisterationForm()
        return render(request, "account/register.html", context={"form":form})
    def post(self, request):
        pass

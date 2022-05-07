from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class HomeView(View):
    def post(self):
        pass
    def get(self, request):
        return render(request, "home/index.html")


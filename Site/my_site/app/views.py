from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.http import request
from django.template.response import TemplateResponse
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

from .models import Articles , User , Category

# Create your views here.

class Register(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"

def main(request):
    return render(request, 'main.html')


def news(request):
    return render(request, 'news.html')


def articles(request):
    return render(request, 'articles.html')


def help(request):
    return render(request, 'help.html')


def about(request):
    return render(request, 'about.html')


'''бллок регистрации ...'''




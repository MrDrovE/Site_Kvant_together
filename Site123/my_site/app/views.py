from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.http import request
from django.template.response import TemplateResponse
from django.views.generic import DetailView
from .models import Articles

# Create your views here.
def main(request):
    return render(request, 'main.html')


def news(request):
    news = Articles.objects.order_by('-date')[:10]
    return render(request, 'news.html',{'news':news})

class NewsDatailView(DetailView):
    model = Articles
    template_name = 'news_detail.html'
    context_object_name = 'Article'


def articles(request):
    return render(request, 'articles.html')


def help(request):
    return render(request, 'help.html')


def about(request):
    return render(request, 'about.html')


'''бллок регистрации ...'''




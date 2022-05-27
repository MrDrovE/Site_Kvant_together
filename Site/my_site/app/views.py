from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.http import request
from django.template.response import TemplateResponse
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy

from .models import Articles, Comments
from .forms import CommentForm


# Create your views here.
def main(request):
    news = Articles.objects.order_by('?')[:3]
    sixblock = Articles.objects.order_by('-date')[:6]
    return render(request, 'main.html', {'news1': news[0],'news2': news[1],'news3': news[2],
                                         'sixblock1': sixblock[0],'sixblock2': sixblock[1],'sixblock3': sixblock[2],'sixblock4': sixblock[3]})

def news(request):
    news = Articles.objects.order_by('-date')[:10]
    return render(request, 'news.html', {'news': news})

class NewsDatailView(FormMixin, DetailView):
    model = Articles
    template_name = 'news_detail.html'
    context_object_name = 'Article'
    form_class = CommentForm
    success_msg = 'Коментарий успешно создан'

    def get_context_data(self, **kwards):
        context = super(NewsDatailView, self).get_context_data(**kwards)
        context['Comments'] = Comments.objects.order_by('-create_date')[:5]
        return context

    def get_success_url(self):
        return reverse_lazy('NewsDatail', kwargs={'pk': self.get_object().id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.post_id = self.get_object()
        self.object.author_id = self.request.user
        self.object.save()
        return super().form_valid(form)

def help(request):
    return render(request, 'help.html')

def about(request):
    return render(request, 'about.html')

    '''бллок регистрации ...'''

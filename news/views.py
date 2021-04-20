from django.http import HttpResponse
from django.shortcuts import render
from .models import Article

# Create your views here.

def index(request):
    context_dict = {}
    articles = Article.objects.all()
    context_dict['articles'] = articles
    return render(request, "index.html", context=context_dict)
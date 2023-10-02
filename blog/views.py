from django.http import HttpResponse
from django.shortcuts import render
from .db_articles import articles


def home_view(request):
    #return HttpResponse('Hello World !')
    return render(request, 'home.html')

def contact_view(request):
    #return HttpResponse('Contactez-nous.')
    return render(request, 'contact.html')

def article_view(request):
    #return HttpResponse('La page des articles')
    return render(request, 'article.html', context={'articles':articles})
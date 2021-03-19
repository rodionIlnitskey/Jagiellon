import json
from django.views import View
from django.contrib.contenttypes.models import ContentType
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Article, Comment
from django.urls import reverse


def index(request):
    latest_comments_list = Comment.objects.all()[::-1]
    return render(request, 'articles/index.html', {'latest_comments_list': latest_comments_list})

def leave_comment(request):
    Comment.objects.create(author_name = request.POST['name'], comment_text = request.POST['text'])
    return HttpResponseRedirect( reverse('articles:index') )

def opis(request):
    return render(request, 'articles/opis.html')

def authorpost(request, pk):
    post = get_object_or_404(Comment, pk=pk)
    return render(request, 'articles/authorpost.html', {'post': post})

def account(request):
    return render(request, 'articles/account.html')

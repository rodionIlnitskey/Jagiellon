import json
from django.views import View
from django.contrib.contenttypes.models import ContentType
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Article, Comment
from django.urls import reverse
from .forms import PostForm
from django.shortcuts import redirect

def index(request):
    latest_comments_list = Comment.objects.all()[::-1]
    return render(request, 'articles/index.html', {'latest_comments_list': latest_comments_list})

"""def leave_comment(request):
    Comment.objects.create(author_name = request.POST['name'], comment_text = request.POST['text'])
    return HttpResponseRedirect( reverse('articles:index') )"""

"""def opis(request):
    return render(request, 'articles/opis.html')"""

def authorpost(request, pk):
    post = get_object_or_404(Comment, pk=pk)
    return render(request, 'articles/authorpost.html', {'post': post})

def account(request):
    return render(request, 'articles/account.html')

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('articles:index')
    else:
        form = PostForm()
    return render(request, 'articles/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Comment, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('articles:authorpost', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'articles/post_edit.html', {'form': form})
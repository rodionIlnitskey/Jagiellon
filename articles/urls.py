from django.urls import path

from django.conf.urls import url
from django.contrib.auth.decorators import login_required
 
from . import views
from .models import Article, Comment


app_name="articles"
urlpatterns = [
    path('', views.index, name = 'index'),
    #path('opis', views.opis, name = 'opis'),
    #path('leave_comment', views.leave_comment, name = 'leave_comment'),
    path('account', views.account, name = 'account'),
    path('post/<int:pk>/', views.authorpost, name = 'authorpost'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/new/', views.post_new, name='post_new'),

]

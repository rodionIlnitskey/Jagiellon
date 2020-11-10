from django.urls import path
from . import views

app_name="articles"
urlpatterns = [
    path('', views.index, name = 'index'),
    path('opis', views.opis, name = 'opis'),
    path('leave_comment', views.leave_comment, name = 'leave_comment'),
]

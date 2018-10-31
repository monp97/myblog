from django.urls import path,re_path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    #re_path(r'^blogs/([0-9])/$',views.open_blog,name='open_blog')
    re_path(r'^articles/([0-9])/$', views.open_blog,name='open_blog'),
]

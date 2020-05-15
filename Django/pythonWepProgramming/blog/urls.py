"""pythonWepProgramming URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
# from bookmark.views import PostLV, PostDV, PostAV, PostYAV, PostMAV, PostDAV, PostTAV 
from blog import views


# 한글 슬러그를 위해 re_path()사용
app_name = 'blog'
urlpatterns = [
    # /blog/
    path('', views.PostLV.as_view(), name = 'index'),

    #/blog/post/
    path('post/', views.PostLV.as_view(), name = 'post_list'),

    #/blog/post/django-example
    path(r'^post/(?P<slug>[-\w]+)/$',views.PostDV.as_view(), name = 'post_detail'),

    #/blog/archive
    path('archive/', views.PostAV.as_view(), name = 'post_archive'),

    #/blog/archive/2019/
    path('archive/<int:year>/', views.PostYAV.as_view(), name = 'post_year_archive'),

    #/blog/archive/2019/nov/
    path('archive/<int:year>/<int:month>/', views.PostMAV.as_view(), name = 'post_month_archive'),

    #/blog/archve/2019/nov/10/
    path('archive/<int:year>/<int:month>/<int:day>/', views.PostDAV.as_view(), name = 'post_day_archive'),

    #/blog/archive/today/
    path('archive/totay/', views.PostTAV.as_view(), name = 'post_today_archive'),
]

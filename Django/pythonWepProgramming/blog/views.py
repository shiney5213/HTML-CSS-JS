from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView
from blog.models import Post

# Create your views here.

# ListView
class PostLV(ListView):
    model = Post
    template_name = 'blog/templates/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2

#DetailView
class PostDV(DetailView):
    model = Post
    template_name = 'blog/templates/post_detail.html'


# ArchiveView
class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_dt'
    template_name = 'blog/templates/post_archive.html'



class PostYAV(YearArchiveView):
    model = Post
    date_filed = 'modefy_dt'
    make_object_list = True

class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modity_dt'

class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_dt'

class PostTAV(TodayArchiveView):
    model = Post
    Dete_field = 'modify_dt'
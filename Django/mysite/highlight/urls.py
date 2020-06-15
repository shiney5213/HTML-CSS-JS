from django.urls import path
from . import views



urlpatterns = [
    path('', views.highlightView.as_view(), name = 'highlight'),
    path('subtitle', views.subtitleView.as_view(), name = 'subtitle'),
    path('subtitle/makesubtitle', views.makesubtitleView.as_view(), name = 'makesubtitle'),
    # path('output', views.output),



]
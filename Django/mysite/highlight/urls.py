from django.urls import path
from . import views



urlpatterns = [
    path('', views.highlightView.as_view(), name = 'highlight'),
    path('highlightgraph', views.highlightgraphView.as_view(), name = 'highlight'),

    path('highlightgraph/subtitle', views.subtitleView.as_view(), name = 'subtitle'),
    path('highlightgraph/subtitle/makesubtitle', views.makesubtitleView.as_view(), name = 'makesubtitle'),
    path('analysis', views.analysis),
    path('savevideo', views.savevideo),
    path('startSearch', views.startSearch),
    # path('currentTime', views.currentTime),
    # path('output', views.output),



]